# TP3

## Questions

- **2 ->** 524 paquets de 1040 octets aquités en 5 secondes -> 0.87 Mb/s
  En UDP il n'y a pas de fiabilité sur l'ordre et l'arrivée des paquets, la méthode de calcul sur les numéros d'ACK ne fonctionne donc pas

- **3 ->** 38 paquets de 1040 octets aquités en 5 secondes -> 0.06 Mb/s

- **4 ->** Temps de propagation plus long -> plus de chances de croiser un autre paquet -> plus de collisions -> plus de perte

- **5 ->** 0.87 + 0.06 = 0.93 -> 93% d'utilisation du lien -> opérateur réseau content, utilisateurs du flux 1 contents, utilisateurs du flux 2 pas contents

- **6 ->** De 7 à 10s -> ACK 92 à ACK 379 -> 287 paquets de 1040 octets en 3 secondes -> 0.80 Mb/s
  C'est 13% moins bien en moyenne que de 0 à 5 et d'après un petit test ça vient clairement de la taille des buffers de n2 et n3
