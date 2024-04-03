"""in polymorphism their is 2 things one is overloading and one is overriding
Polymorphism means same function name (but different signature) beign uses for different types"""

#Example of defination would be:

'''l=[10,20,30,40]
print(len(l))
s="Welcome"
print(len(s))'''
#In above example len() is a built in function but we can also define our own functions with the same name.
#In this example we can see different uses of same function this is exactly what polymorphism is

#overloading
'''class Ws:
    def displayinfo(self,name=" "):
        print("Welcome to WS cubetech"+name)
obj=Ws()
obj.displayinfo()
obj.displayinfo(' python')'''

#overriding

class Ws:
    def displayinfo(self):
        print("Welcome to Wscubetech")
class IIP(Ws):
    def displayinfo(self):
        #super().displayinfo() #We can use this function to call parent function also.
        print("Welcome to IIP")#overriding means when same name of child function override the parents function.
obj=IIP()
obj.displayinfo()