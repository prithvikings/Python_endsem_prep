#Directory
"""Directionary is an unordered collection(but now its ordered) and have key-value pairs.
In python dictionaries are defined within curly braces{} with each item 
being a pair in the form key:value
dict-name={key:value}
indexing & slicing not work
insertion order is preserved
any kinds of elements are allowed
mutable in nature(we can change value)
key must be unique but value duplicate allowed"""
d={"name":"Prithvi","Age":17,"name":"Rohit","Password":"Rohit123"}
print(d,type(d))
print(d["Age"])
print(d.get("Password"))
print(d.get("Passwordggf","Not Available")) #Agar Key Galat hoga to yeh not available show karega
print(d.get("Password","Not Available"))
print(d.keys())
print(d.values())
print(d.items())
for key, values in d.items():
    print(key,values,sep="-")
d["Age"]=50
print(d)
print(d.pop("Age"))
print(d)
(d.clear())
print(d)

#for changing value
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]=2020
print(car)

#for adding any value in dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"]='blue'
print(thisdict)