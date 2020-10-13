main : main.o SequenceCirculaire.o
	g++ -o main main.o SequenceCirculaire.o -std=c++11 -Wall -Weffc++ -g

main.o : main.cpp
	g++ -c main.cpp -std=c++11 -Wall -Weffc++ -g

SequenceCirculaire.o : SequenceCirculaire.cpp
	g++ -c SequenceCirculaire.cpp -std=c++11 -Wall -Weffc++ -g

run :
	./main

clean :
	rm main main.o SequenceCirculaire.o
