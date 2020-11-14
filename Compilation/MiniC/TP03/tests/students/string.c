#include "printlib.h"

int main() {
    string s,s2;
    s2 = "titi";
    println_string(s);
    s = s + "toto";
    println_string(s);
    s = s + ", " + s2;
    println_string(s);
    return 0;
}

// EXPECTED
//
// toto
// toto, titi
