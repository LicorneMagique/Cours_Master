laClasse : LaClasse.o
	g++ -o laClasse LaClasse.o
	echo laClasse > .gitignore
	echo LaClasse.o >> .gitignore
LaClasse.o : LaClasse.cpp
	g++ -c LaClasse.cpp -std=c++11
	echo laClasse > .gitignore
	echo LaClasse.o >> .gitignore
run :
	./laClasse

clean :
	rm laClasse LaClasse.o
