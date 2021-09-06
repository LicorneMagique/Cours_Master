import std.stdio;
import std.concurrency;
import core.time;
import std.algorithm;
import std.random;

struct CancelMessage {}

bool isDebug() {
    // return true;
    return false;
}

struct Noeud {
    Tid tid; // thread_ID
    int lid; // logical_ID
    int state; // état : 1 candidat, 2 perdu, 3 élu
    int leaderId; // logical_ID du leader connu
}

struct Liste {
    int[] liste;
}

void receiveAllFinalization(Noeud [] childTid) {
    for (int i = 0; i < childTid.length; ++i) {
        receiveOnly!CancelMessage();
    }
}

void spawnedFunc(int myId) {
    Noeud myself, neighbor;

    receive((immutable(Noeud) myself_, immutable(Noeud) neighbor_) {
        myself = cast(Noeud)myself_;
        neighbor = cast(Noeud)neighbor_;
    });

    writeln("Child process: I am number ", myId, ", my neighbor id is ", neighbor.lid);

    // Phase d'élection
    if (myId > neighbor.lid) {
        if (isDebug()) {
            writeln("Child process: I am number ", myId, ", je me présente pour les élections");
        }
        myself.state = 1;
        myself.leaderId = myId;
        send(neighbor.tid, myId, true);
    }
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
                    if (isDebug()) {
                        writeln("Child process: I am number ", myId, ", j'ai perdu les élections");
                    }
                    send(neighbor.tid, precLeaderId, true);
                } else if (myId == precLeaderId) {
                    myself.state = 3;
                    if (isDebug()) {
                        writeln("Child process: I am number ", myId, ", j'ai gagné les élections");
                    }
                    send(neighbor.tid, myId, false);
                }
            } else {
                myself.leaderId = precLeaderId;
                if (isDebug()) {
                    writeln("Child process: I am number ", myId, ", le gagnant est le ", precLeaderId);
                }
                send(neighbor.tid, precLeaderId, false);
                loop = false;
            }
        });
    }

    // Comptage
    int myIndex = 0;
    int n;
    if (myself.state == 3) {
        if (isDebug()) {
            writeln("Child process: I am number ", myId, ", je commence le compte");
        }
        send(neighbor.tid, 1);
    }
    receive((int count) {
        if (myself.state == 3) {
            n = count;
            if (isDebug()) {
                writeln("Child process: I am number ", myId, ", le compte termine à ", count);
            }
        } else {
            myIndex = count;
            if (isDebug()) {
                writeln("Child process: I am number ", myId, ", le compte en est à ", count);
            }
            send(neighbor.tid, ++count);
        }
    });

    // Re-numérotation des noeuds
    if (myself.state == 3) {
        Liste ids = Liste(getRandomIds(n, n));
        writeln("Child process: I was number : ", myId, ", my new ID is ", ids.liste[myIndex]);
        myself.lid = ids.liste[myIndex];
        myId = ids.liste[myIndex];
        send(neighbor.tid, cast(immutable)ids);
    } else {
        receive((immutable(Liste) ids) {
            writeln("Child process: I was number ", myId, ", my new ID is ", ids.liste[myIndex]);
            myself.lid = ids.liste[myIndex];
            myId = ids.liste[myIndex];
            if (myIndex < ids.liste.length) {
                send(neighbor.tid, cast(immutable)ids);
            }
        });
    }

    send(ownerTid, CancelMessage());
}

int[] getRandomIds(int n, int bigN) {
    int[] ids = new int[bigN];
    Random random = Random(unpredictableSeed); // prod
    // Random random = Random(42); // debug
    for (int i = 0; i < bigN; ++i) {
        ids[i] = i;
    }
    ids = ids.randomShuffle(random);
    writeln("ids ", ids[0..n]);
    return ids[0..n];
}

void main() {
    const int n = 10;
    const int bigN = 20;

    // Création des noeuds
    Noeud[] childTid = new Noeud[n];
    int[] ids = getRandomIds(n, bigN);
    for (int i = 0; i < n; ++i) {
        childTid[i].tid = spawn(&spawnedFunc, ids[i]);
        childTid[i].lid = ids[i];
    }

    // Envoi des informations aux noeuds
    for (int i = 0; i < n; ++i) {
        const int neighborIndex = (i + 1) % n;
        immutable(Noeud) itself = cast(immutable)childTid[i];
        immutable(Noeud) neighbor = cast(immutable)childTid[neighborIndex];
        send(childTid[i].tid, itself, neighbor);
    }

    receiveAllFinalization(childTid);

}
