"""write a program to  fill in a letter template given below with ammeand  date
letter=
         '''dear<name>
        you are seected!!
                         <date>'''
"""


letter='''Dear<|Name|>,
            Namaskar Bro
              you are selected!

                     Date:<|Date|>
'''
name=input("Enter Your Name:\n")
date=input("Enter the Date:\n")
letter=letter.replace("|Name|",name)
letter=letter.replace("|Date|",date)
print(letter)

