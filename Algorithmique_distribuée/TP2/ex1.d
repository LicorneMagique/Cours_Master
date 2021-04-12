// mport std.c.time;
import std.stdio;
import std.concurrency;
import core.time;
import std.algorithm;
import std.random;

struct CancelMessage {
}

struct Noeud {
    Tid tid; // thread_ID
    int lid; // logical_ID
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

int[] getRandomIds(int n) {
    int[] ids = new int[n];
    Random random = Random(unpredictableSeed); // prod
    // Random random = Random(42); // debug
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

    // spawn threads (child processes)
    Noeud[] childTid = new Noeud[n];
    int[] ids = getRandomIds(n);
    for (int i = 0; i < n; ++i) {
        childTid[i].tid = spawn(&spawnedFunc, ids[i], n);
        childTid[i].lid = ids[i];
    }

    // create an unidirectional ring
    for (int i = 0; i < n; ++i) {
        // id of neighbor
        // WORK: correct this part of code
        const int nextIndex = (i + 1) % n;
        // const int nextId = ids[nextIndex];
        // end of your code

        immutable(Noeud) id_suiv = cast(immutable)childTid[nextIndex];
        // send id_suiv to childTid[i].tid
        send(childTid[i].tid, id_suiv);
    }

    // nombre de noeuds
    send(childTid[3].tid, 0, -1, cast(shared) new int[0]);

    // wait for all completions
    receiveAllFinalization(childTid);

}

/*
  Combien d’anneaux unidirectionnels différents existe-t’il (on notera n le nombre
  de nœuds dans l’anneau et on supposera, par exemple, que la numérotation 0 (numéro de
  p1) - 1 (numéro de p2) - 2 (numéro de p3) est différente de 1 (numéro de p1) - 2 (numéro de
  p2) - 0 (numéro de p3)) ?
  n = 1 -> 2 éléments -> ab, ba -> 2 anneaux
  n = 2 -> 3 éléments -> abc, acb, bac, bca, cab, cba -> 6 anneaux
  Il y a (n-1)! anneaux.
*/
