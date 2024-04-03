"""values=[(int(input()),) for _ in range (int(input()))]
values=[(value[0], value[0]**2) for value in values]
print(values)"""













#square symbol pattern 
"""row=int(input("Enter No. of Rows: "))
column=int(input("Enter No. of columns: "))
symbol=input("Enter Your fav Symbol: ")
for i in range(row):
    for j in range(column):
        print(symbol,end="")
    print()"""


#ascending type of pattern
"""row=int(input("Enter number rows:"))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end="")
    print()"""




#decreasing pattern
"""row=int(input("Enter Your Rows: "))
symbol=input("Enter Your fav symbol: ")
for i in range(row):
    for j in range(i,row):
        print(symbol,end=" ")
    print()"""



#another right side trianler
"""row=int(input("Enter Rows: "))
for i in range(row):
    for j in range(i+1,):
        print("",end=" ")
    for j in range(i,row):
        print("@",end="")
    print()"""

#right sided triangle

"""row=int(input("Enter rows: "))
for i in range(row):
    for j in range(i,row):
        print("",end=" ")
    for j in range(i+1):
        print("*",end="")
    print()"""








#Wordfinder
"""user_input=input("Enter ")
if user_input=="123123":
    print("Valid")
else:
    print("Invalid")"""




"""user_input1=input("Enter a string: ")
char_input=input("Enter a character to count: ")

count=0

for char in user_input1:
    if char==char_input:
        count+=1
print(f"The character {char_input} appears {count} times in the string")"""



"""user_input=input("Enter a string: ")
char_count=input("Enter character: ")
count=0
for char in user_input:
    if char==char_count:
        count+=1
print(f"In {user_input} the {char_count} appears {count} times in string" )"""


"""reverse indexing
tuple square"""

# Generating a tuple containing squares of numbers from 1 to 5
"""numbers = (1, 2, 3, 4, 5)

# Creating a tuple of squares using list comprehension
squared_tuple = tuple(x ** 2 for x in numbers)

print(squared_tuple)"""

