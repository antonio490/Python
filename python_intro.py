## Quick python introduction

# Lists
# A list can contain a misture of other types as its elements, including strings, tuples,
# lists, dictionaries, functions, file objects and any type of number.

x = ["first", "second", "third", "fourth"]

# x[0] prints out "first"
print(x[0])

# x[-4] prints out "first"
print(x[-4])

# x[1:-1] prints out ["second", "third"]
print(x[1:-1])

# x[0:4] prints out ["first", "second", "third", "fourth"]
print(x[0:4])

print(len(x))

print(x.reverse())

# Tuples
# Tuples are similar to lists but they are immutable. They cant be modified after
# they habe been created.

x = [1,2,3,4]
y = (1,2,3,4)

# Conversion between both types of variables
tupla = tuple(x)
lista = list(y)

# Dictionaries
# Dictionaries provides associative array functionality implemented using hash types

x = {1: "one", 2: "two"}

x["first"] = "one"

x[("Madrid", "Antonio", 1992)] = (1,2,3)

# [1, 2, 'first', ('Madrid', 'Antonio', 1992)]
print(list(x.keys()))

# one
print(x[1])

# two
print(x.get(2))

# not available
print(x.get(4, "not available"))

# Strings

