CXXFLAGS=-Wall -Werror -Wfatal-errors -std=c++17
CXX=clang++


main: main.o Person.o
	$(CXX) -o main main.o Person.o

main.o: main.cc Person.h
	$(CXX) -c $(CXXFLAGS) main.cc

Person.o: Person.cc Person.h
	$(CXX) -c $(CXXFLAGS) Person.cc

clean:
	rm -rf *.o main
