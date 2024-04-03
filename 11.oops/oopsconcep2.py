"""CONSTRUCTOR IS TYPE OF METHOD WHERE WE DONT NEED TO CALL 
IT IT ALREADY CALLED WHEN WE CREATE OBJECT"""

class DemoClass:
    a=10
    def showvalue(self):
        self.c=self.a*self.a
        print(self.c)

    def showvalue1(self):
        print("Welcome to india")

    def showvalue2(self,a,b):
        print(a+b)

obj=DemoClass()
obj.showvalue()
obj.showvalue1()
obj.showvalue2(20,15)