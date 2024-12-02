#
# File paths
# COMP 1701 
# A. Fedoruk
# 
# 

# Usually you want to open any files using *relative* paths. That is, 
# you specify the file relative to the current working directory. 
# e.g. 

file = 'stormy.txt'

# But if you have a file in a subdirectory or need to use a relative 
# path, you run up into the path separator issue. Windows uses \ and 
# the rest of the world uses /. 

# Lets say I am running on a Windows machine and I have a file in my H drive directory 
# 1701 called stormy.txt

# How can I open it? 

file = "H:\1701\stormy.txt"

# file_handle = open(file)

# Well that didn't work.
# Lets print the file name to see what it going on: 

print(file)

# Remember that \ is a special character in Python strings that is used 
# to escape other characters, \n - newline, \t - tab or \000 0 octal character. 
# \ followed by three numbers is an octal (base 8) representation of a character. 
# In this case \170 in the string is actually a lower case x. Not helpful 
# to open the file.  


# There are several ways to fix this. 

# 1) Create a 'raw' string by prefixing the string with an r. 
#    The r tells the interpreter to give no special meaning to the 
#    \, it is now just a backslash. 

file = r'H:\1701\stormy.txt'
print(file)
file_handle = open(file)
file_handle.close()

# 2. Use forward slashes. 

file = "H:/1701/stormy.txt"
print(file)
file_handle = open(file)
file_handle.close()

# Python will do the conversion between / and \ for you based on 
# your OS. This is the preferred method. 

# If you need more sophisticated file handling you can use the 
# pathlib module. 
