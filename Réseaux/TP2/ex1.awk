BEGIN {
}

{
    event = $1;
    time = $2; # en secondes
    src_H2 = $3;
    dst_H2= $4;
    type = $5;
    size = $6; # en octets
    idflow = $8;
    src_H3=$9;
    dst_H3=$10;
    idseq=$11;
    idpaquet = $12;

    ######## VOTRE CODE ICI ########
    if ( event == "+" && type == "cbr" ) {
        if (departs[idseq] == "") {
            departs[idseq] = time;
        }
    } else if ( event == "r" && type == "cbr") {
        arrivees[idseq] = time;
        delais[idseq] = time - departs[idseq];
        if (delais[idseq -1] != "") {
            gigues[idseq] = delais[idseq] - delais[idseq -1];
        }
    }
    ###############################
}

END {
    avg1 = 0;
    avg2 = 0;
    for (i in gigues) {
        if (i <= 120) {
            avg1 += gigues[i];
        } else if (i > 125 && i <= 300) {
            avg2 += gigues[i];
        }
    }
    avg1 /= 120;
    avg2 /= 175;

    avg3 = (delais[120] - delais[0]) / 120
    avg4 = (delais[300] - delais[125]) / 175

    print "133 : départ =", departs[133], ", arrivée =", arrivees[133], "délai =", delais[133];
    print "134 : départ =", departs[134], ", arrivée =", arrivees[134], "délai =", delais[134];
    print "135 : départ =", departs[135], ", arrivée =", arrivees[135], "délai =", delais[135];
    print "gigue 134 :", gigues[134], ", gigue 135 :", gigues[135];
    print "de 0 à 120 :", avg1, ", de 125 à 300 :", avg2;
    print "de 0 à 120 :", avg3, ", de 125 à 300 :", avg4, "(méthode 2)";
    print "done";
}
