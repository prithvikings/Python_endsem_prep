#SET
"""A set is an unordered collection of items.
Every set element is unique (no duplicates) and must be
mutable (can be changed)
it also used curly braces {}
it also delete duplicate element by its own
In sets insertion order is not preserved
indexing and slicing not work in sets
In sets we can add hetrogenous elements are allowed"""

my_set={7,4,3,7,True}
print(my_set)
print()
my_set.add("raju")
print(my_set)
print()
my_set.update(["prithvi","good","boy"])
print(my_set,type(my_set))
print()
print(my_set.pop())
print()
print(my_set.pop)
print()
print(my_set)
print()
my_set.remove(4)
print(my_set)
print()
my_set.clear
print(my_set)
print()
var={10,'prithvi',56.0,True,'prithvi',56.0,'rohit',100}
var2={10,'prithvi',56.0,True,'prithvi',56.0,'india',False}
print(var.union(var2))
print()
print(var.intersection(var2))
print()
print(var.difference(var2))
print()
print(var-var2)