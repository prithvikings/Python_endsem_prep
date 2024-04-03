# Loop Control Statements = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop.
# pass =        does nothing, acts as a placeholder

"""user_input=input("Enter Your name")
while user_input=="":
    print("You have Not Entered Your Name")
    user_input=input("Enter Your name")
print(f"Hello {user_input}")"""




phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)