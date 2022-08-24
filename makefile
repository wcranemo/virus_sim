CFLAGS=-Wall -Werror -Wfatal-errors

main: main.o Person.o
	g++ -o main main.o Person.o

main.o: main.cc Person.h
	g++ -c $(CFLAGS) main.cc

Person.o: Person.cc Person.h
	g++ -c $(CFLAGS) Person.cc

clean:
	rm -rf *.o main
