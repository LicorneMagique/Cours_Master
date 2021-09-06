#include "printlib.h"

int main() {

    println_int(3/0);
    println_int(3%0);

    return 0;
}

// EXPECTED
// EXITCODE 1
// Division by 0
