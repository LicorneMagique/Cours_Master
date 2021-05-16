// import std.c.time;
import std.stdio;
import std.concurrency;
import core.time;
import std.algorithm;
import std.random;

struct CancelMessage {
    int algoSentMsgCount;
    int algoReceivedMsgCount;
}

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

CancelMessage receiveAllFinalization(Noeud [] childTid) {
    int algoSentMsgCount = 0;
    int algoReceivedMsgCount = 0;
    for (int i = 0; i < childTid.length; ++i) {
        const CancelMessage msg = receiveOnly!CancelMessage();
        algoSentMsgCount += msg.algoSentMsgCount;
        algoReceivedMsgCount += msg.algoReceivedMsgCount;
    }
    if (isDebug()) {
        writeln("Nombre de messages envoyés ", algoSentMsgCount);
        writeln("Nombre de messages reçus ", algoReceivedMsgCount);
        writeln("Différence ", algoReceivedMsgCount - algoSentMsgCount);
    }
    return CancelMessage(algoSentMsgCount, algoReceivedMsgCount);
}

void spawnedFunc(int myId, int n) {
    Noeud myself, neighbor;
    int algoSentMsgCount = 0;
    int algoReceivedMsgCount = 0;

    // waiting for the reception of information sent by the father
    receive((immutable(Noeud) myself_, immutable(Noeud) neighbor_) {
        myself = cast(Noeud)myself_;
        neighbor = cast(Noeud)neighbor_;
    });

    if (isDebug()) {
        writeln("Child process: I am number ", myId, ", my neighbor id is ", neighbor.lid);
    }

    // Phase d'élection
    receive((int one) {
        algoReceivedMsgCount++;
        if (one != 1) {
            writeln("On a un problème");
        }
        if (isDebug()) {
            writeln("Child process: I am number ", myId, ", je me présente pour les élections");
        }
        myself.state = 1;
        myself.leaderId = myId;
        send(neighbor.tid, myId, true);
        algoSentMsgCount++;
    });

    bool loop = true;
    while (loop) {
        receive((int precLeaderId, bool elec) {
            algoReceivedMsgCount++;
            if (elec) {
                if (myId > precLeaderId) {
                    if (myself.state != 1) {
                        myself.state = 1;
                        send(neighbor.tid, myId, true);
                        algoSentMsgCount++;
                    }
                } else if (myId < precLeaderId) {
                    myself.state = 2;
                    myself.leaderId = precLeaderId;
                    if (isDebug()) {
                        writeln("Child process: I am number ", myId, ", j'ai perdu les élections");
                    }
                    send(neighbor.tid, precLeaderId, true);
                    algoSentMsgCount++;
                } else if (myId == precLeaderId) {
                    myself.state = 3;
                    if (isDebug()) {
                        writeln("Child process: I am number ", myId, ", j'ai gagné les élections");
                    }
                    send(neighbor.tid, myId, false);
                    algoSentMsgCount++;
                }
            } else {
                myself.leaderId = precLeaderId;
                if (isDebug()) {
                    writeln("Child process: I am number ", myId, ", le gagnant est le ", precLeaderId);
                }
                send(neighbor.tid, precLeaderId, false);
                algoSentMsgCount++;
                loop = false;
            }
        });
    }

    send(ownerTid, CancelMessage(algoSentMsgCount, algoReceivedMsgCount));
}

int[] getRandomIds(int n) {
    int[] ids = new int[n];
    Random random = Random(unpredictableSeed); // prod
    // Random random = Random(42); // debug
    for (int i = 0; i < n; ++i) {
        ids[i] = i;
    }
    ids = ids.randomShuffle(random);
    if (isDebug()) {
        writeln("ids ", ids);
    }
    return ids;
}

CancelMessage doExecution(int n) {
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
    return receiveAllFinalization(childTid);
}

void main() {
    int sentCount = 0,
        receivedCount = 0,
        minSent = -1,
        minReceived = -1,
        maxSent = -1,
        maxReceived = -1;
    const int n = 20; // number of child processes
    const int k = 100; // Nombre de simulations

    for (int i = 0; i < k; ++i) {
        const CancelMessage msg = doExecution(n);
        sentCount += msg.algoSentMsgCount;
        receivedCount += msg.algoReceivedMsgCount;
        if (minSent == -1) {
            minSent = msg.algoSentMsgCount;
            minReceived = msg.algoReceivedMsgCount;
            maxSent = msg.algoSentMsgCount;
            maxReceived = msg.algoReceivedMsgCount;
        }
        if (msg.algoSentMsgCount < minSent) {
            minSent = msg.algoSentMsgCount;
        }
        if (msg.algoReceivedMsgCount < minReceived) {
            minReceived = msg.algoReceivedMsgCount;
        }
        if (msg.algoSentMsgCount > maxSent) {
            maxSent = msg.algoSentMsgCount;
        }
        if (msg.algoReceivedMsgCount > maxReceived) {
            maxReceived = msg.algoReceivedMsgCount;
        }
    }
    writeln("Meilleur cas (envoyé) : ", minSent, " messages, ", double(minSent) / double(n) , " message/thread");
    writeln("Meilleur cas (reçu) : ", minReceived, " messages, ", double(minReceived) / double(n), " message/thread");
    writeln("Pire cas (envoyé) : ", maxSent, " messages, ", double(maxSent) / double(n), " message/thread");
    writeln("Pire cas (reçu) : ", maxReceived, " messages, ", double(maxReceived) / double(n) , " message/thread");
    writeln(
        "Nombre moyen de messages envoyé : ", sentCount / k, ", ",
        (double(sentCount) / double(k)) / double(n), " messages/thread"
    );
    writeln(
        "Nombre moyen de messages reçu : ", receivedCount / k, ", ",
        (double(receivedCount) / double(k)) / double(n), " messages/thread"
    );
}
