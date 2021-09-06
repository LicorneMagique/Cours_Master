# instantiation du simulateur
set ns [new Simulator]

# instantiation du fichier de traces
set file1 [open out.tr w]
$ns trace-all $file1

# instantiation du fichier de traces pour NAM
set file2 [open out.nam w]
$ns namtrace-all $file2

# procédure pour lancer automatiquement le visualisateur
# NAM à la fin de la simulation
proc finish {} {
    global ns file1 file2
    $ns flush-trace
    close $file1
    close $file2
    exec nam out.nam &
    exit 0
}

# instantiation de quatre noeuds
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]

# instantiation d’une ligne de communication full duplex
# entre les noeuds n0 et n1
$ns duplex-link $n0 $n2 2Mb 10ms DropTail
$ns duplex-link $n1 $n2 2Mb 10ms DropTail
$ns duplex-link $n2 $n3 1.5Mb 20ms DropTail

# déclaration de flux TCP
set tcp [new Agent/TCP]
$ns attach-agent $n0 $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n3 $sink
$ns connect $tcp $sink

# instantiation d’une connexion UDP sur n1
set udp [new Agent/UDP]
$ns attach-agent $n1 $udp
set null [new Agent/Null]
$ns attach-agent $n3 $null
$ns connect $udp $null
$udp set fid_ 1  # permet d’associer un identifiant a ce flot

#instantiation d'une connexion FTP
set ftp [new Application/FTP]
$ftp attach-agent $tcp
# scénario de début et de fin de génération des paquets par ftp
$ns at 2.0 "$ftp start"
$ns at 4.0 "$ftp stop"

# instantiation d’un trafic CBR composé de paquets de
# 1000 octets, générés toutes les 8 ms -> 1Ko à 1Mb/s
set cbr0 [new Application/Traffic/CBR]
$cbr0 attach-agent $udp
$cbr0 set packetSize_ 1000
$cbr0 set interval_ 0.008

# scénario de début et de fin de génération des
# paquets par cbr0
$ns at 1 "$cbr0 start"
$ns at 5 "$cbr0 stop"

# la simulation va durer 5 secondes de temps simulé
$ns at 5.0 "finish"

# début de la simulation
$ns run
