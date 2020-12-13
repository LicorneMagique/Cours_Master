#include "printlib.h"

int main() {

    bool b;
    b = true;
    println_int(b); // 1
    println_int(false); // 0
    println_int(false || true); // 1
    println_int(true || false); // 1
    println_int(false && true); // 0
    println_int(true && false); // 0
    println_int(!true); // 0
    println_int(!false); // 1
    println_int(!(true)); // 0
    println_int(!(false)); // 1
    b = (!(true || false) && !(false || !true));
    println_int(b); // 0
    b = (!(!true || false) && (false || true));
    println_int(b); // 1
    return 0;
}

// EXPECTED
// 1
// 0
// 1
// 1
// 0
// 0
// 0
// 1
// 0
// 1
// 0
// 1
