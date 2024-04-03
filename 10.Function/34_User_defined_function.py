#What is Function?
"""A function is a block of statements which can be used reptitively in a program.It saves
the time of a developer. In Python concept of function is same as in other languages"""

"""You Can Pass data known as parameters into a function"""

#Sample function
#function with arguments
#function with return

"""In function we just have to create function or define function then we have to call them according to our use"""
#For writing function we start with def then we give any name to function and then two bracket and colon

def simplefunction():
    print("Hello,Duniya!")
simplefunction()


#Function With Arguments

def argument(a,b):
    print("Sum: ",a+b)


argument(2,4)

#default value in function

def sum(a,b=5):
    print(a+b)
sum(20) #in this if we pass only one data then computer will take other data from upper function
sum(4,6)#agar hum log alag se yaha data daal denge to yeh overwrite kar dega


#Return Function
def square(x):
    return(x*x)
s=square(5)
print(s)
