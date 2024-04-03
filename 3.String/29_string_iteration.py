a="Hello World"
t=len(a)
print(t)
print()
for n in range (t):
    print(a[n])

#a[0]=H
#a[1]=e

#reverse iteration
#This is One Way for Reverse
b="Hello World"
b=b[-1::-1]
p=len(b)
print(p)
print()
for j in range (p):
    print(b[j])
print()


#Another Way
b="Hello World"
p=len(b)
print(p)
print()
for j in range (p-1,-1,-1):
    print(b[j])
print()


#Another Way to iterate
w="Welcome to wscubetech"
for a in w:
    print(a)

#Another way to reverse
w="Welcome to wscubetech"
w=w[-1::-1]
for a in w:
    print(a)
