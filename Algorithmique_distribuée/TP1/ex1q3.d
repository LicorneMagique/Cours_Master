module ex1q3;

import std.stdio;
import std.concurrency;

void spawnedFunc(Tid parentTid) {
    writeln("Child process: on vient de me créer avec ", parentTid);
    for (int ack = 0; ack < 3; ack++) {
        receive((int i) {
            writeln("Child process: I have received the number ", i);
            if (ack == 2) {
                send(parentTid, 1);
                writeln("Child process: je viens d'envoyer un acquittement");
            }
        });
    }
}

void main() {
    // Start spawnedFunc in a new thread.
    auto childTid = spawn(&spawnedFunc, thisTid);

    writeln("Parent process: I have just sent 3 messages to the child process ");
    send(childTid, 42);
    send(childTid, 43);
    send(childTid, 44);

    receive((int i) {
        writeln("Parent process: je viens de récupérer un acquittement : ", i);
    });
}
