#include "printlib.h"

int main() {
    int x,i,k;
    x = 1;
    k = 3000;
    while (x < k) {
        x = 2 * x;
        i = i + 1;
    }
    println_int(x);
    println_int(i);
    return 0;
}

// EXPECTED
// 4096
// 12
