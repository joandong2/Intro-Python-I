"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
f = open("c:/Users/user/Desktop/LAMBDA/Computer Science/Intro-Python-I/src/foo.txt", "r")
print(f.read())
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
f = open("c:/Users/user/Desktop/LAMBDA/Computer Science/Intro-Python-I/src/bar.txt", "w")
f.write("Do you bite your thumb at us, sir?\nI do bite my thumb, sir.\nDo you bite your thumb at us, sir?")
f.close()

f = open("c:/Users/user/Desktop/LAMBDA/Computer Science/Intro-Python-I/src/bar.txt", "r")
print(f.read())
f.close()
