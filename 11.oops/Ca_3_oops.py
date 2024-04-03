"""class DemoClasss:
    a=10
    def __init__(self):
        print("wwelcome")
    def showvalue (self):
        self.c=self.a*self.a
        print(self.c)
    def showvalue1(self,a,b):
        print(a,b)

obj=DemoClasss()
obj.showvalue()
obj.showvalue1(20,30)"""

#Inheritence
"""class A:
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
obj.displayc()"""

#Encapsculation
"""class student:
    def __init__(self):
        self.__name=""
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
obj=student()
obj.setname("Hello")
name=obj.getname()
print(name)"""

#otherencapsculation
"""class Student:
    def __init__(self):
        print("prithvi")
    def display(self,a,b):
        print("This is prithvi",a)
        print("Hello Ji",b)
obj=Student()
obj.display(20,15)"""

#polymorphism

#overloading
"""class Ws:
    def displayinfo(self,name=" "):
        print("Welcome to WS cubetech"+name)
obj=Ws()
obj.displayinfo()
obj.displayinfo(' python')"""

#overriding

"""class Ws:
    def displayinfo(self):
        print("Welcome to Wscubetech")
class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()
        print("Welcome to IIP")
obj=IIP()
obj.displayinfo()"""