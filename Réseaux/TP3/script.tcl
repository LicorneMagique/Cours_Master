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

# instantiation des noeuds
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]

# instantiation des lignes de communication
$ns duplex-link $n0 $n2 1Mb 10ms DropTail
$ns duplex-link $n1 $n2 1Mb 10ms DropTail
$ns duplex-link $n2 $n3 1Mb 10ms DropTail
$ns duplex-link $n3 $n4 1Mb 50ms DropTail

# déclaration des flux TCP
set tcp1 [new Agent/TCP]
set tcp2 [new Agent/TCP]
$ns attach-agent $n0 $tcp1
$ns attach-agent $n1 $tcp2
set sink1 [new Agent/TCPSink]
set sink2 [new Agent/TCPSink]
$ns attach-agent $n3 $sink1
$ns attach-agent $n4 $sink2
$ns connect $tcp1 $sink1
$ns connect $tcp2 $sink2

#instantiation des connexions FTP
set ftp1 [new Application/FTP]
set ftp2 [new Application/FTP]
$ftp1 attach-agent $tcp1
$ftp2 attach-agent $tcp2
# scénario de début et de fin de génération des paquets par ftp
$ns at 0.0 "$ftp1 start"
$ns at 0.0 "$ftp2 start"
$ns at 5.0 "$ftp1 stop"
$ns at 10.0 "$ftp2 stop"

# Taille des buffers
$ns queue-limit $n2 $n3 10
$ns queue-limit $n3 $n2 10

# la simulation va durer 5 secondes de temps simulé
$ns at 10.0 "finish"

# début de la simulation
$ns run
