"""Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit1. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data1."""
class student:
    def __init__(self):
        self.__name=""
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
obj=student()
obj.setname("Hello")
name=obj.getname()
print(name)
