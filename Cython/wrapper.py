from ctypes import cdll
lib = cdll.LoadLibrary('./libexample.so')



class Person(object):
    def __init__(self):
        self.obj = lib.Person_new()

    def greet(self):
        lib.Person_greet(self.obj)


p = Person()
p.greet()