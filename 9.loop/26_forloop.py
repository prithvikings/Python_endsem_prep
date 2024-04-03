#For loop with range()

#Range is predefine function which is used for numbers only 
#range(5)
#start=0
#condition<5
#increment 1
#0,1,2,3,4

#range(1,6)
#start=1
#condition<6
#increment 1
#1,2,3,4,5

#range(1,6,2)
#start=1
#condtion<6
#increment 2
#1,3,5

for n in range(1):
    print(n)
print()#we are using this to just give space and get result spacely to understand

for n in range(1,6):
    print(n)
print()#same here like above

for n in range(1,6,2):
    print(n)
print()

#table of 2
for a in range(2,21,2):
    print(a)
print()
#Another way of writing table
for a in range(1,11):
    print(a*2)
print()
#Another way
for a in range(1,11):
    print("2*",a,"=",a*2)
print()

#Range for reverse
for a in range(10,0,-1):
    print(a)
print()




for a in range(1,11):
    print()
