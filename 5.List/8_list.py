#LIST
"""Lis is an ordered sequence of items
it is one of the most used datatype in python and is very flexible
it can store any kind of data"""
#And is used from []
ls=[1,2.2,'ws']
li=[1,3,'ws']
li[2]=10
print(ls,type(ls))
print(li,type(li))
a=[1,2,3.5,[8,9,10]]#Example of nested list
print(a[3][2])

#Example of slicing
b=[2.3,4,'six',True,[0,3,4]]
print(b[1:5])
print(b[0:])
print(b[0::2])
print(b[-1::-2])
c=[2.6,4,'six',True,[0,3,4]]
c[3]="hello"
print(c[-1::-1])

