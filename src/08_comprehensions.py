"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
for x in range(1, 6):
    y.append(x)
print(y)
# y = [i for i in range(6)]

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []
for x in range(10):
    y.append(x**3)
print(y)
# y = [i**3 for i in range(10)]

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]
y = []
for str in range(len(a)):
    y.append(a[str].upper())
print(y)
# y = [s.upper() for s in a]

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = []
for num in range(len(x)):
    if(int(x[num]) % 2) == 0:
        y.append(x[num])
print(y)

# y = [i for i in x if i % 2 == 0]
# for i in x:
#   if i % 2 == 0
#       y.append(i)
