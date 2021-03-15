module ex2;

// mport std.c.time;
import std.stdio;
import std.concurrency;
import core.time;
import std.algorithm;

struct CancelMessage {
}

struct Noeud {
    Tid tid; // hread_ID
    int lid; // ogical_ID
}

void receiveAllFinalization(Noeud [] childTid) {
    for (int i = 0; i < childTid.length; ++i) {
        receiveOnly!CancelMessage();
    }
}

void spawnedFunc(int myId, int n) {

    Noeud neighbor, localNeighbor;
    int[] vectHorloge = new int[n];
    for (int i = 0; i < n; i++) {
        vectHorloge[i] = 0;
    }
    int scalHorloge = 1;
    vectHorloge[myId] = 1;
    writeln("Child process: I am number ", myId, ", my scalHorloge is ", scalHorloge);
    writeln("Child process: I am number ", myId, ", my vectHorloge is ", vectHorloge);

    // waiting for the reception of information sent by the father
    receive((immutable(Noeud) neighbor) {
        localNeighbor = cast(Noeud)neighbor;
    });
    scalHorloge++;
    vectHorloge[myId]++;
    writeln("Child process: I am number ", myId, ", my scalHorloge is ", scalHorloge);
    writeln("Child process: I am number ", myId, ", my vectHorloge is ", vectHorloge);

    // WORK: print your id and your neighbor id
    writeln("Child process: I am number ", myId, ", my neighbor id is ", localNeighbor.lid);

    // comptage
    receive((int count, int precScalHorloge, shared int[] precVectHorloge) {
        scalHorloge = max(++scalHorloge, ++precScalHorloge);
        for (int i = 0; i < precVectHorloge.length; i++) {
            if (precVectHorloge[i] > vectHorloge[i]) {
                vectHorloge[i] = precVectHorloge[i];
            }
        }
        vectHorloge[myId]++;
        writeln("Child process: I am number ", myId, ", le compte en est à ", count);
        writeln("Child process: I am number ", myId, ", my scalHorloge is ", scalHorloge);
        writeln("Child process: I am number ", myId, ", my vectHorloge is ", vectHorloge);
        send(localNeighbor.tid, ++count, scalHorloge, cast(shared) vectHorloge);
    });

    // comptage
    receive((int count, int precScalHorloge, shared int[] precVectHorloge) {
        scalHorloge = max(++scalHorloge, ++precScalHorloge);
        for (int i = 0; i < precVectHorloge.length; i++) {
            if (precVectHorloge[i] > vectHorloge[i]) {
                vectHorloge[i] = precVectHorloge[i];
            }
        }
        vectHorloge[myId]++;
        writeln("Child process: I am number ", myId, ", le compte final en est à ", count);
        writeln("Child process: I am number ", myId, ", my scalHorloge is ", scalHorloge);
        writeln("Child process: I am number ", myId, ", my vectHorloge is ", vectHorloge);
        send(localNeighbor.tid, count, scalHorloge, cast(shared) vectHorloge);
    });

    // Avec cette technique il y a 2 * n messages échangés pour compter les noeuds
    // end of your code

    send(ownerTid, CancelMessage());

}


void main() {
    // number of child processes
    int n = 10;

    // spawn threads (child processes)
    Noeud[] childTid = new Noeud[n];
    for (int i = 0; i < n; ++i) {
        childTid[i].tid = spawn(&spawnedFunc, i, n);
        childTid[i].lid = i;
    }

    // create an unidirectional ring
    for (int i = 0; i < n; ++i) {
        // id of neighbor
        // WORK: correct this part of code
        const int next = (i + 1) % n;
        // end of your code

        immutable(Noeud) id_suiv = cast(immutable)childTid[next];
        // send id_suiv to childTid[i].tid
        send(childTid[i].tid, id_suiv);
    }

    // nombre de noeuds
    send(childTid[3].tid, 0, -1, cast(shared) new int[0]);

    // wait for all completions
    receiveAllFinalization(childTid);

}
