main : main.o Expression.o
	g++ -o main main.o Expression.o
	echo main > .gitignore
	echo main.o >> .gitignore
	echo Expression.o >> .gitignore
main.o : main.cpp
	g++ -c main.cpp -std=c++11
	echo main > .gitignore
	echo main.o >> .gitignore
	echo Expression.o >> .gitignore
Expression.o : Expression.cpp
	g++ -c Expression.cpp -std=c++11
	echo main > .gitignore
	echo main.o >> .gitignore
	echo Expression.o >> .gitignore
run :
	./main

clean :
	rm main main.o Expression.o
