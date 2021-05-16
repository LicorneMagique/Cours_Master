// import std.c.time;
import std.stdio;
import std.concurrency;
import core.time;
import std.algorithm;
import std.random;

/*
  Hypothèses
    • Chaque nœud a un identifiant unique et sait que les identifiants sont uniques
    • Chaque nœud connaît son voisin
    • Le nombre de nœuds dans le système est inconnu de chaque nœud
*/

struct CancelMessage {}

struct Noeud {
    Tid tid; // thread_ID
    int lid; // logical_ID
    int state; // état : 1 candidat, 2 perdu, 3 élu
    int leaderId; // logical_ID du leader connu
}

void receiveAllFinalization(Noeud [] childTid) {
    for (int i = 0; i < childTid.length; ++i) {
        receiveOnly!CancelMessage();
    }
}

void spawnedFunc(int myId, int n) {
    Noeud myself, neighbor;

    // waiting for the reception of information sent by the father
    receive((immutable(Noeud) myself_, immutable(Noeud) neighbor_) {
        myself = cast(Noeud)myself_;
        neighbor = cast(Noeud)neighbor_;
    });

    // WORK: print your id and your neighbor id
    writeln("Child process: I am number ", myId, ", my neighbor id is ", neighbor.lid);

    // Phase d'élection
    receive((int one) {
        if (one != 1) {
            writeln("On a un problème");
        }
        writeln("Child process: I am number ", myId, ", je me présente pour les élections");
        myself.state = 1;
        myself.leaderId = myId;
        send(neighbor.tid, myId, true);
    });

    bool loop = true;
    while (loop) {
        receive((int precLeaderId, bool elec) {
            if (elec) {
                if (myId > precLeaderId) {
                    if (myself.state != 1) {
                        myself.state = 1;
                        send(neighbor.tid, myId, true);
                    }
                } else if (myId < precLeaderId) {
                    myself.state = 2;
                    myself.leaderId = precLeaderId;
                    writeln("Child process: I am number ", myId, ", j'ai perdu les élections");
                    send(neighbor.tid, precLeaderId, true);
                } else if (myId == precLeaderId) {
                    myself.state = 3;
                    writeln("Child process: I am number ", myId, ", j'ai gagné les élections");
                    send(neighbor.tid, myId, false);
                }
            } else {
                myself.leaderId = precLeaderId;
                writeln("Child process: I am number ", myId, ", le gagnant est le ", precLeaderId);
                send(neighbor.tid, precLeaderId, false);
                loop = false;
            }
        });
    }

    // Phase de notification
    // receive();
    // leaderId = receivedNumber;
    // send(neighbor, true, receivedNumber);

    send(ownerTid, CancelMessage());
}

int[] getRandomIds(int n) {
    int[] ids = new int[n];
    // Random random = Random(unpredictableSeed); // prod
    Random random = Random(42); // debug
    for (int i = 0; i < n; ++i) {
        ids[i] = i;
    }
    ids = ids.randomShuffle(random);
    writeln("ids ", ids);
    return ids;
}


void main() {
    // number of child processes
    int n = 10;
    // int n = 32678; // core.thread.threadbase.ThreadError@src/core/thread/threadbase.d(1219): Error creating thread
    // int n = 32677; // Fonctionne

    // spawn threads (child processes)
    Noeud[] childTid = new Noeud[n];
    int[] ids = getRandomIds(n);
    for (int i = 0; i < n; ++i) {
        childTid[i].tid = spawn(&spawnedFunc, ids[i], n);
        childTid[i].lid = ids[i];
    }

    // create an unidirectional ring
    for (int i = 0; i < n; ++i) {
        const int neighborIndex = (i + 1) % n;
        immutable(Noeud) itself = cast(immutable)childTid[i];
        immutable(Noeud) neighbor = cast(immutable)childTid[neighborIndex];
        // send nodes to child
        send(childTid[i].tid, itself, neighbor);
    }

    // Élection
    for (int i = 0; i < n; i++) {
        send(childTid[i].tid, 1);
    }

    // wait for all completions
    receiveAllFinalization(childTid);
}
