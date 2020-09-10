main : Generateur.o
	g++ -o main Generateur.o
	echo main > .gitignore
	echo Generateur.o >> .gitignore
Generateur.o : Generateur.cpp
	g++ -c Generateur.cpp -std=c++11
	echo main > .gitignore
	echo Generateur.o >> .gitignore
run :
	./main

clean :
	rm main Generateur.o
