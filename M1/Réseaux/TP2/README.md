# TP2

## Exercice 1

- **1 ->** J'ai un doute sur le délai de bout-en-bout, on va supposer que ce délai se mesure à partir de t_0 et non à partir de t_envoi_du_paquet  
Dans la mesure où `g_n = d_n - d_n-1` où `d_n` délai de bout-en-bout, alors `d_n` est le dernier paquet envoyé et `d_n-1` est l'avant dernier paquet envoyé, à priori `d_n-1` est arrivé avant `d_n` donc `d_n > d_n-1` donc `g_n > 0`  
La gigue est une quantité plutôt **positive**

- **2 ->** Je suppose que c'est important de connaître la gigue pour toutes les applications qui doivent gérer un **flux en direct**, donc surtout le streaming ou les communications **audio et vidéo**

- **3 ->** Mon numéro de séquence `211` apparaît pour la première fois sur cette ligne `+ 2.688 1 2 cbr 1000 ------- 1 1.0 3.1 211 300` donc à t=2.688s et avec l'identifiant de paquet 300

- **4 ->** gigue 134 : `0.00288s` , gigue 135 : `-0.002667s`

- **5 ->** de 0 a 120 : `0` , de 125 a 300 : `8.96e-05s`, on peut en conclure que ça sert à rien, l'écart type serait intéressant

- **6 ->** Finalement le calcul de la gigue ne dépent pas des paquets intermédiaires, seulement du premier et du dernier paquet

  ```text
  g1 = b1 - b0
  g2 = b2 - b1
  g3 = b3 - b2

  g_moy = (g1 + g2 + g3) / 3
  g_moy = ((b1 - b0) + (b2 - b1) + (b3 - b2)) / 3
  g_moy = (- b0 + b1 - b1 + b2 - b2 + b3) / 3
  g_moy = (- b0 + b3) / 3

  g_moy = (b_n -b0) / n
  ```

- **7 ->** J'implémente ma formule `g_moy = (b_n -b0) / n`

- **8 ->** Je n'ai pa du tout les mêmes résultats ce qui est très bizarre...  
De 0 à 120 : `-0.00852156` , de 125 à 300 : `8.96e-05`

## Exercice 2

- **2 ->** Partie importante du script `awk` (ex2.awk)

  ```awk
  if (src == 2 && dest == 3) {
      if (event == "+") {
          buffer++;
      } else if (event == "-" || event == "d") {
          buffer--;
      }
      print time, buffer;
  }
  ```

  Ligne de commande pour le lancer

  ```shell
  awk -f ex2.awk out2.tr > buffer.out
  ```

- **3 ->** Script `gnuplot` (buffer.gnu)

  ```plot
  # le fichier "buffer.out" contient les valeurs à tracer
  # trace la courbe (colonne 2 en fonction de la colonne 1) avec style 1 et titré "courbe 1"
  plot "buffer.out" using 1:2 title "courbe 1" with lines ls 1

  # ajoute une seconde courbe (colonne 3 fonction de colonne 1) avec style 2 et titré "courbe 2"
  replot "buffer.out" using 1:3 title "courbe 3" with lines ls 2

  # légendes des axes
  set xlabel "temps"
  set ylabel "fenetre de congestion"
  replot

  # pour sauvegarder le graphe dans un fichier postscript
  set term png
  set output "buffer.png"
  replot
  ```

- **4 ->** Il y a 3 pics de saturation du buffer, TCP qui régule son trafic ?

  ![buffer](buffer.png)

- **4 ->** Ajouts au script awk

  ```awk
  # Dans le bloc BEGIN
  avg_0_5 = 0;
  avg_2_4 = 0;

  # Dans le bloc du milieu
  if (lastBuffer != "") {
      avg_0_5 += lastBuffer * (time - lastTime);
  }
  if (time >= 2 && time <= 4) {
      if (lastBuffer != "") {
          avg_2_4 += lastBuffer * (time - lastTime);
      }
  }
  lastBuffer = buffer;
  lastTime = time;

  # Dans le bloc END
  avg_0_5 /= 5;
  avg_2_4 /= 2;
  print "Moyenne de 0 à 5 :", avg_0_5;
  print "Moyenne de 2 à 4 :", avg_2_4;
  ```

  Résultats

  ```text
  Moyenne de 0 à 5 : 1.79008
  Moyenne de 2 à 4 : 4.444
  ```
