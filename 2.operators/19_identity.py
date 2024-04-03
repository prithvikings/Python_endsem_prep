#identity operator:-(is,is not)
a=5
b=5
print(a is b)#true
#for checking the id we can use
print("id of a : ", id(a))
print("id of b : ", id(b))
c=8
d=9
print(c is d)#false
print(c is not d)#true
print("id of c : ",id(c))
print("id of d : ",id(d))