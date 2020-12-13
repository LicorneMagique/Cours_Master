#include "printlib.h"

int main() {

    println_int(4 / 3);
    println_int((-4) / 3);
    println_int(4 / (-3));
    println_int((-4) / (-3));
    println_int(4 % 3);
    println_int((-4) % 3);
    println_int(4 % (-3));
    println_int((-4) % (-3));
    println_int(4 * 3);
    println_int(4 * (4));
    println_int(4 * 4 * 4);
    println_int(4 + 3 * 3);
    println_int((4 + 3) * 3);

    return 0;
}

// EXPECTED
// 1
// -1
// -1
// 1
// 1
// -1
// 1
// -1
// 12
// 16
// 64
// 13
// 21
