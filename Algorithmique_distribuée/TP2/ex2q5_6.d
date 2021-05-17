// import std.c.time;
import std.stdio;
import std.concurrency;
import core.time;
import std.algorithm;
import std.random;
import std.typecons: tuple, Tuple;

struct CancelMessage {
    int nbMsg;
    int nbCandidat;
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

struct Stats {
    int nbMsg;
    int nbCandidat;
    int min;
    int max;
    double avg;
}

Stats receiveAllFinalization(Noeud [] childTid) {
    int nbMsg = 0;
    int nbCandidat = 0;
    int min = -1;
    int max;
    double avg;
    for (int i = 0; i < childTid.length; ++i) {
        const CancelMessage msg = receiveOnly!CancelMessage();
        nbMsg += msg.nbMsg;
        nbCandidat += msg.nbCandidat;
        if (min == -1) {
            min = msg.nbMsg;
            max = msg.nbMsg;
        }
        if (msg.nbMsg < min) {
            min = msg.nbMsg;
        }
        if (msg.nbMsg > max) {
            max = msg.nbMsg;
        }
    }
    avg = double(nbMsg) / double(childTid.length);
    if (isDebug()) {
        writeln("Nombre de messages envoyés ", nbMsg);
        writeln("Nombre de candidats ", nbCandidat);
    }
    return Stats(nbMsg, nbCandidat, min, max, avg);
}

bool getRandomBoolean() {
    Random random = Random(unpredictableSeed);
    return uniform(0, 2, random) == 1;
}

void spawnedFunc(int myId, int n) {
    Noeud myself, neighbor;
    const bool candidat = getRandomBoolean();
    int nbMsg = 0;
    int nbCandidat = candidat ? 1 : 0;

    // waiting for the reception of information sent by the father
    receive((immutable(Noeud) myself_, immutable(Noeud) neighbor_) {
        myself = cast(Noeud)myself_;
        neighbor = cast(Noeud)neighbor_;
    });

    if (isDebug()) {
        writeln("Child process: I am number ", myId, ", my neighbor id is ", neighbor.lid);
    }

    // Phase d'élection
    if (candidat) {
        if (isDebug()) {
            writeln("Child process: I am number ", myId, ", je me présente pour les élections");
        }
        myself.state = 1;
        myself.leaderId = myId;
        send(neighbor.tid, myId, true);
        nbMsg++;
    }

    bool loop = true;
    while (loop) {
        receive((int precLeaderId, bool elec) {
            if (elec) {
                if (myId > precLeaderId) {
                    if (myself.state != 1) {
                        myself.state = 1;
                        send(neighbor.tid, myId, true);
                        nbMsg++;
                    }
                } else if (myId < precLeaderId) {
                    myself.state = 2;
                    myself.leaderId = precLeaderId;
                    if (isDebug()) {
                        writeln("Child process: I am number ", myId, ", j'ai perdu les élections");
                    }
                    send(neighbor.tid, precLeaderId, true);
                    nbMsg++;
                } else if (myId == precLeaderId) {
                    myself.state = 3;
                    if (isDebug()) {
                        writeln("Child process: I am number ", myId, ", j'ai gagné les élections");
                    }
                    send(neighbor.tid, myId, false);
                    nbMsg++;
                }
            } else {
                myself.leaderId = precLeaderId;
                if (isDebug()) {
                    writeln("Child process: I am number ", myId, ", le gagnant est le ", precLeaderId);
                }
                send(neighbor.tid, precLeaderId, false);
                nbMsg++;
                loop = false;
            }
        });
    }
    send(ownerTid, CancelMessage(nbMsg, nbCandidat));
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

Stats doExecution(int n) {
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

    // wait for all completions
    return receiveAllFinalization(childTid);
}

Tuple!(int[][int], int, int, int, int) getValuesFromExections(int n, int k) {
    int min = -1;
    int max;
    int nbMsg = 0;
    int nbCandidat = 0;
    int[][int] values;
    for (int i = 0; i < k; ++i) {
        const Stats stat = doExecution(n);
        nbMsg += stat.nbMsg;
        nbCandidat += stat.nbCandidat;
        if (min == -1) {
            min = stat.nbMsg;
            max = stat.nbMsg;
        }
        if (stat.nbMsg < min) {
            min = stat.nbMsg;
        }
        if (stat.nbMsg > max) {
            max = stat.nbMsg;
        }
        values[stat.nbCandidat] = values.require(stat.nbCandidat, []) ~ [stat.nbMsg];
    }
    return tuple(values, min, max, nbMsg, nbCandidat);
}

Stats[int] getStatsFromValues(int[][int] values) {
    Stats[int] stats;
    foreach (int valuesKey; values.keys) {
        stats[valuesKey] = stats.require(valuesKey, Stats(-1, -1, -1, -1, -1));
        int min = -1;
        int max;
        int sum = 0;
        foreach (int nbMsg; values[valuesKey]) {
            if (min == -1) {
                min = nbMsg;
                max = nbMsg;
            }
            if (nbMsg < min) {
                min = nbMsg;
            }
            if (nbMsg > max) {
                max = nbMsg;
            }
            sum += nbMsg;
        }
        stats[valuesKey].min = min;
        stats[valuesKey].max = max;
        stats[valuesKey].avg = double(sum) / double(values[valuesKey].length);
    }
    return stats;
}

void main() {
    int nbMsg = 0;
    int minSent = -1;
    int maxSent = -1;
    int nbCandidat = 0;
    const int n = 20; // number of child processes
    const int k = 500; // Nombre de simulations
    // const int k = 50; // debug

    auto res = getValuesFromExections(n, k);
    int[][int] values = res[0];
    minSent = res[1];
    maxSent = res[2];
    nbMsg = res[3];
    nbCandidat = res[4];

    Stats[int] stats = getStatsFromValues(values);

    writeln("Candid.\tAvg\tMin\tMax");
    foreach (int statsKey; stats.keys.sort) {
        writeln(statsKey, "\t", stats[statsKey].avg, "\t", stats[statsKey].min, "\t", stats[statsKey].max);
    }

    writeln("\nMeilleur cas : ", minSent, " messages, ", double(minSent) / double(n) , " message/thread");
    writeln("Pire cas : ", maxSent, " messages, ", double(maxSent) / double(n), " message/thread");
    writeln(
        "Nombre moyen de messages : ", nbMsg / k, ", ",
        (double(nbMsg) / double(k)) / double(n), " messages/thread"
    );
    writeln(
        "Nombre moyen de candidats par tour : ", nbCandidat / k, ", ",
        double(nbCandidat) / double(k * n) , " candidat/thread"
    );
}
