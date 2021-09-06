import std.stdio;
import std.concurrency;

void spawnedFunc(Tid parentTid) {
    // Receive a message from the owner thread.
    receive((int i) {
        writeln("Child process: I have received the number ", i);
        send(parentTid, 1);
        writeln("Child process: je viens d'envoyer un acquittement");
    });
    writeln("Child process: on vient de me créer ", parentTid);
    // send(parentTid, "Done");
}

void main() {
    // Start spawnedFunc in a new thread.
    auto childTid = spawn(&spawnedFunc, thisTid);

    // Send a number to this new thread.
    send(childTid, 42);
    writeln("Parent process: I have just sent a message to the child process ");

    receive((int i) {
        writeln("Parent process: je viens de récupérer un acquittement : ", i);
    });
}
