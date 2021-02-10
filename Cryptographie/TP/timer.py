#PEUT ETRE UTILE POUR LE TP NOTE CAR SOUVENT DEMANDE

import time


class Chrono():

    def __init__(self):
        self.start = time.time()

    def end(self):
        self.end = time.time()

    def __str__(self):
        temps = self.end - self.start
        minutes = int(temps//60)
        secondes = str(temps % 60).split(".")[0]
        milliemes = str(temps).split('.')[1][:4]

        return "{} minutes, {} secondes, {} millièmes".format(
            minutes, secondes, milliemes
        )



# L'init de la class démarre le chrono
hello = Chrono()

# Partie que vous voulez chrono
print(8+8)
time.sleep(5) 

# Ceci stop le chrono
hello.end()

# Affichage du Chrono
print(hello)


