#Inheritence

"""Inheritance is a core concept in object-oriented programming (OOP) that allows one class to derive or inherit the properties and methods from another class"""
class A:
    def displayA(Self):
        print("Welcome1")
class B(A):
    def displayB(Self):
        print("Welcome2")
class c(B):
    def displayc(Self):
        print("Hello ji")

obj=c()
obj.displayA()
obj.displayB()
obj.displayc()