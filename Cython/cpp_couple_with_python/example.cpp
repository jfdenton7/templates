#include <iostream>

class Person {
    public:
        void greet() {
            std::cout << "Hello!" << std::endl;
        }
};


extern "C" {
    Person* Person_new() { return new Person(); }
    void Person_greet(Person* p) { p->greet(); }
}

/*
===================================
compiling down to a shared library
===================================

g++ -c -fPIC example.cpp -o example.o
g++ -shared -Wl,-soname,libexample.so -o libexample.so  example.o

*/