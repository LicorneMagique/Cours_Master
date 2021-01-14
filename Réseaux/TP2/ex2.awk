BEGIN {
    buffer = 0;
    steps_0_5 = 0;
    avg_0_5 = 0;
    avg_2_4 = 0;
}

{
    event = $1;
    time = $2; # en secondes
    src = $3;
    dest = $4;
    type = $5;
    size = $6; # en octets
    idflow = $8;
    src_H3=$9;
    dst_H3=$10;
    idseq=$11;
    idpaquet = $12;

    if (src == 2 && dest == 3) {
        if (event == "+") {
            buffer++;
        } else if (event == "-" || event == "d") {
            buffer--;
        }
        steps_0_5++;
        avg_0_5 += buffer;
        if (time >= 2 && time <= 4) {
            steps_2_4++;
            avg_2_4 += buffer;
        }
        print time, buffer;
    }
}

END {
    avg_0_5 /= steps_0_5;
    avg_2_4 /= steps_2_4;
    print "Moyenne de 0 à 5 :", avg_0_5;
    print "Moyenne de 2 à 4 :", avg_2_4;
}
