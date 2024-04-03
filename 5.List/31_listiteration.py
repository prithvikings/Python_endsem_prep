#In this process we are using Range
a=[1,2,3,5,"prithvi"]
t=len(a)
print(t)
print()
for n in range(t):
    print(a[n])
print()

#Here we are doing it in easy way and its direct
c=[1,3,4,6]
for n in (c):
    print(n)
print()

#for reverse we have to use range method
l=[1,3,9,4,7]
t=len(l)
for n in range(t-1,-1,-1):
    print(l[n])
