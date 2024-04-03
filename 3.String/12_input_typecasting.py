#Input
a=input("Enter The Value1:- ")
b=input("Enter the value2:- ")
print(a,type(a))
print(a + b,type(a+b))
"""We can see here that its not adding because its thinking it is
string"""

"""Now We will use typecasting"""

#Typecasting

"""For int"""
a=int(input("Enter the value1:- "))
b=int(input("Enter the value2:- "))
print(a+b,type(a+b))

"""For float"""
a=float(input("Enter the value:- "))
b=float(input("Enter the value:- "))
print(a+b,type(a+b))

"""Eval Can do both"""
a=eval(input('Enter value:- '))
b=eval(input('enter the value:- '))
print(a+b)