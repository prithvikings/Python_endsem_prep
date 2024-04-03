"""Write a program to accept the marks of 6 students and display them in a sorted manner"""

f1=int(input("Enter marks of student Number 1: "))
f2=int(input("Enter marks of student Number 2: "))
f3=int(input("Enter marks of student Number 3: "))
f4=int(input("Enter marks of student Number 4: "))
f5=int(input("Enter marks of student Number 5: "))
f6=int(input("Enter marks of student Number 6: "))

mylist=[f1,f2,f3,f4,f5,f6]
mylist.sort()
print(mylist)