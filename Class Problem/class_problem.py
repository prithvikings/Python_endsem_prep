"""Write a program to read the password from a user 
if user types the correct password i.e python then display
welcome python programing 
note:only three attempts are allowed to enter the right password"""


correct_password = 'python'

attempts = 3
for i in range(attempts):
    
    password = input('Enter your password: ')

    
    if password == correct_password:
        print('Welcome to the Python programming!')
        break
    else:
        
        print('Warning: Incorrect password. Please try again.')
        if i == attempts - 1:
            print('Exceeded maximum login attempts. Please try again later.')





