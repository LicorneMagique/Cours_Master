import std.stdio;
import std.concurrency;

void spawnedFunc() {
    // Receive a message from the owner thread.
    receive((int i) {
        writeln("Child process: I have received the number ", i);
    });
}

void main() {
    // Start spawnedFunc in a new thread.
    auto childTid = spawn(&spawnedFunc);

    // Send a number to this new thread.
    send(childTid, 196);
    writeln("Parent process: I have just sent a message to the child process ");
}

// Foncions importantes : send et receive
