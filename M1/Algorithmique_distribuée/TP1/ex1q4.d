import std.stdio;
import std.concurrency;

void spawnedFunc(Tid parentTid) {
    writeln("Child process: on vient de me créer avec ", parentTid);
    bool ack = false;
    while (!ack) {
        receive((int i) {
            writeln("Child process: I have received the number ", i);
            if (i == 196) {
                send(parentTid, 1);
                writeln("Child process: je viens d'envoyer un acquittement");
                ack = true;
            }
        });
    }
}

void main() {
    // Start spawnedFunc in a new thread.
    auto childTid = spawn(&spawnedFunc, thisTid);

    writeln("Parent process: I am sending messages to the child process");
    send(childTid, 42);
    send(childTid, 43);
    send(childTid, 44);
    send(childTid, 196);

    receive((int i) {
        writeln("Parent process: je viens de récupérer un acquittement : ", i);
    });
}
