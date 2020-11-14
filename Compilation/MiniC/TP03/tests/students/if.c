#include "printlib.h"

int main() {
    bool x;
    x = true;
    if (x) {
        println_string("yes");
    }
    x = !x;
    if (x) {
        println_string("yes");
    } else {
        println_string("no");
    }
    return 0;
}

// EXPECTED
// yes
// no
