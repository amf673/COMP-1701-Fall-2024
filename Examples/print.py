# 
# Using print()
#
# A. Fedoruk
# 

# printing string literals 

print("Hello, World!")
print('Hello World!') 

# printing multiple string literals 

print("Hello,", "World!")

# controlling the spacing between printed arugments

print("Hello,", "World!", sep="")   # note the lack of spacing between the words
print("Hello,", "World!", sep="   ")   # note the extra spacing between the words
print("Hello", "World", "Python", "is", "Fun", sep=", ")

# printing numeric literals

print(42)
print(2,4,8,16,32,64)
print(2,4,8,16,32,64, sep=", ")

print(3.14)

# printing mixed literals 

print( "The value of pi is ", 3.14)
print( "The powers of two are ", 1, 2, 4, 8, 16, 32, 64, "...")

# printing variables
# create some variables 

pi = 3.14 
animal = "Capybara"
year = 2020
i = 0
number = -56.78
large_number = 149597828677.28
avogadros_number = 6.02214076e23
small_number = 0.00000000005145

print("I met a", animal, "in", year)
print("The value of pi is", pi)
print("One AU equals", large_number, "meters")
print("A very small number is", small_number) # note the use of scientific notation. 
print("Avogadros Number is", avogadros_number, "in reciprocal moles")

# using escape sequences

# Adding a newline 
print("Hello,\nWorld")
print("Hello", "World", "And", "All", "The", "Beings", "On", "It", sep="\n")
print("Hello, \n\n\nWorld!")

# Adding tabs 
print("Hello\tWorld")
print(animal, "\t", animal)

# Including quotes in strings 
print("It's")
print('It\'s')
print("Python is \"Fun\"")

# Changing end of line behaviour
print("Hello", end="\n") # default behaviour 
print("world")

print("Hello", end="") # Continue on same line
print("World")

print("Hello", end="\n\n\n")
print("World")

print("Hello", end=" END")
print("World")




