# Exemple de script gnuplot
# commentaire après un #
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
