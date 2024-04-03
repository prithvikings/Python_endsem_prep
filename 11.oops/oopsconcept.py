"""In oops their is concept of class and object 
in class we can make multiple function variable and methods
class is a blueprint or template of object 
with the help of object we can call class function
and for one class we can create many object

class ke andar jo likhte hai woh method hote hai function bahar v use hote hai"""


class DemoClass:  #Within class we can store variable and function
    a=10

    def sumvalue(self):
        print(20+30)

Demoobject=DemoClass()
Demoobject1=DemoClass()#this is object for Democlass
#But it will not print for printing it we need to
#print object

print(Demoobject.a)
print(Demoobject1.a)
Demoobject.sumvalue()
