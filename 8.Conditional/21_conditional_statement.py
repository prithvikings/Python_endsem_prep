#If statement
"""if[conditional expression]:
         [statement(s) to execute]
         
Example:-"""


#Another example
a=int(input("Enter Value:"))
if a%2==0:
    print(a,"Even Number")


#if else statement
"""
if[conditional expression]:
else:
    [alternate statement to execute]

Example:-"""
a=int(input("Enter Number: "))
if a%2==0:
    print("it's Even Number")
else:
    print("it's Odd Number")
    
#if else elif statement
"""
if[condition #1]:
          [statement #1]
elif[condtion #2]:
          [statement #2]
elif [condition #3]:
          [statement #3]
else:
          [statemnent when if and elif(s) are false]"""
    




print("Your Welcome in Result Calculator")

marks=int(input("Enter Your Marks: "))
if marks>=85:
    print("You Got First division")
elif marks>=65:
    print("You Got Second division")
elif marks>=45:
    print("You Got third division")
else:
    print("You are Failed")
