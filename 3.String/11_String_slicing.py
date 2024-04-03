#greeting="good morning ,"
#name="Prithvi"
#Hum log dono string ko ek sath aise bhi type kr skte hai print(greeting+name)
#Aur dusra tarika yeh hai neeche wala
#c=(greeting+name)
#print(c)
name="prithvi"
print(name[6])
#name[5]="d"--> Does not work

print(name[0:3])
print(name[:5])# is same as [0:5]
c=name[-4:-1] #is same as name[1:4]
print(c)
name2="prithviisgoodboy"
d=name2[0::2] 
'''we can provide a skip value as a part
 of our slice like this and is know as slicing with skip value'''
print(d)