"""
if[condition #1]:
          [statement #1]
elif[condtion #2]:
          [statement #2]
elif [condition #3]:
          [statement #3]
else:
          [statemnent when if and elif(s) are false]
    
Example:-"""
#per=int(input("Enter Your Marks"))
#if per>=60:
    #print("first division")
#elif per>=48:
    #print("Second Div")
#elif per>35:
    #print("Third Div")
#else:
    #print("Fail")


per=int(input("Enter Your Marks:- "))
if per >=60:
    print("Congrats You are 1st divison")
elif per>=48:
    print("You did Well You are 2nd divison")
elif per>=35:
    print("You need to work hard")
else:
    print("Better luck next time You are fail")