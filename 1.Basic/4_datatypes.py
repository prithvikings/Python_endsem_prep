"""python have two type of datatype.
mutable object can change its state or 
contents and immmutable object cannot.
mutable:-list,dictionary,sets,bytearray
immutable:-int,float,string,tuple,complex"""

#NUMBERS
a=5 
print(a,"is of type",type(a)) #5 is type of <class'int'>

a=2.0
print(a,"is of type",type(a)) #2.0 is type <class'float'>

a=1+2j 
print(a,"is of type",type(a)) #is of type <class'complex'>

#STRING

"""A string is a collection of one or more character put in a
single quote,double-quote or triple quote"""
"""multi-line string can be denoted using triple quoted"""


s="This is a string"
print(s,type(s))

s='''A multiline 
string'''
print(s,type(s))

s='''
hello
worlds'''
print(s,type(s))

s='10'
print(s,type(s))#this will be string because 10 has single quotation marks



#LIST
#LIST
"""List is an ordered sequence of items
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


#Tuple
'''Tuple is an ordered sequence of items same as a list
it is defined within parentheses () where items are seprated by 
commas.
Tuple is faster than list and tuple always include more than 1 value and we can not update value in 
tuple
tuple is a data structure which is also called collection of items
in which we can store anything like string,float,integer
In tupple duplicate value are allowed
We can Use Len to find length of tupple'''

t=(5,'program',1+3j)
l=t.index('program')
print(t,type(t))
print(len(t))
print(t[1])
print(l)
t1=(10)
print(t1,type(t1))#we can see here that its showing int becasue tuple must have more than one value

#Directory
"""Directionary is an unordered collection of key-value pairs.
In python dictionaries are defined within braces{} with each item 
being a pair in the form key:value
dict-name={key:value}
indexing & slicing not work
insertion order is preserved
hetrogenous elements are allowed
mutable in nature
key must be unique but value duplicate allowed"""
d={"name":"Prithvi","Age":17,"name":"Rohit","Password":"Rohit123"}
print(d,type(d))
print(d["Age"])
print(d.get("Password"))
print(d.get("Passwordggf","Not Available")) #Agar Key Galat hoga to yeh not available show karega
print(d.get("Password","Not Available"))
print(d.keys())
print(d.values())
print(d.items())
for key, values in d.items():
    print(key,values,sep="-")
d["Age"]=50
print(d)
print(d.pop("Age"))
(d.clear())
print(d)

#SET
"""A set is an unordered collection of items.
Every set element is unique (no duplicates) and must be
mutable (can be changed)
it also used curly braces {}
it also delete duplicate element by its own
In sets insertion order is not preserved
indexing and slicing not woork in sets
In sets we can add hetrogenous elements are allowed"""

my_set={7,4,3,7,True}
my_set.add("raju")
my_set.update(["prithvi","good","boy"])
print(my_set,type(my_set))
print(my_set.pop())
print(my_set.pop)
print(my_set)
my_set.remove(4)
print(my_set)
my_set.clear
print(my_set)
var={10,'prithvi',56.0,True,'prithvi',56.0,'rohit',100}
var2={10,'prithvi',56.0,True,'prithvi',56.0,'india',False}
print(var.union(var2))
print(var.intersection(var2))
print(var.difference(var2))
print(var-var2)
