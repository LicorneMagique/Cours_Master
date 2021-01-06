#include "printlib.h"

int main() {

    int a,b;
    a = 4;
    b = 3;

    if (a < b) { // faux
        println_int(a);
    } else {
        println_int(b);
    }
    if (a > b) { // vrai
        println_int(a);
    } else {
        println_int(b);
    }
    if (a <= b) { // faux
        println_int(a);
    } else {
        println_int(b);
    }
    if (a >= b) { // vrai
        println_int(a);
    } else {
        println_int(b);
    }
    if (a <= a) { // vrai
        println_int(a);
    } else {
        println_int(b);
    }
    if (a >= a) { // vrai
        println_int(a);
    } else {
        println_int(b);
    }
    if (a >= a && b > a) { // faux
        println_int(a);
    } else {
        println_int(b);
    }
    if (false || b > a) { // faux
        println_int(a);
    } else {
        println_int(b);
    }

    return 0;
}

// EXPECTED
// 3
// 4
// 3
// 4
// 4
// 4
// 3
// 3
