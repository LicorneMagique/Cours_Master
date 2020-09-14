main : main.o Tableau.o
	g++ -o main main.o Tableau.o -Wall -Weffc++ -g
	echo main > .gitignore
	echo main.o >> .gitignore
	echo Tableau.o >> .gitignore
main.o : main.cpp
	g++ -c main.cpp -std=c++11 -Wall -Weffc++ -g
	echo main > .gitignore
	echo main.o >> .gitignore
	echo Tableau.o >> .gitignore
Tableau.o : Tableau.cpp
	g++ -c Tableau.cpp -std=c++11 -Wall -Weffc++ -g
	echo main > .gitignore
	echo main.o >> .gitignore
	echo Tableau.o >> .gitignore
run :
	./main && make clean

clean :
	rm main main.o Tableau.o
