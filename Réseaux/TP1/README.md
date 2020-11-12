# TP1

## Exercice 1

- 3 : Un lien full-duplex est un lien où chaque appareil peut émettre et recevoir en même temps

- 3 : Buffer avec politique de rejet des paquets de type Drop Tail : fenêtre sautante

- 4 : Calculer le délai de bout-en-bout pour un paquet du trafic UDP : la vitesse de transmission est de 1 Mb/s avec un délai de propagation de 10 ms. = 0.01s et 1 paquet = 1000o -> délai de propagation + temps detransmission -> 1000*8/10^6 + 0.01 -> 0,018s

- 6 : génération du paquet du UDP 10 : -t 0.55

- 7 : temps d'attente : 0.58 - 0.55 = 0.03s, somme de son temps d’émission (transmission) : 0.598 - 0.58 = 0.018s, délai de propagation : 0.598 - 0.55 = 0.048s

- 8 : En déduire le délai de bout-en-bout du 10ème paquet : 0.018 + 0.03 = 0.048s, cohérent
