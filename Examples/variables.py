# Creating/Declaring variables
# 

a = 6              # Expression on rhs is evaluated, its result type determined and a variable called a is created with that value. 
b = "Hello!"       # rhs expression can be a literal, an expression made up or literals and/or variables.
c = 3.45678910 
d = a * c 

# All variables have three attributes: 
# - A name - must follow syntax and convention rules
# - A type - find the type with type()
# - A current value (find with print()

print()
print("Variable a has value", a, "and type", type(a))
print("Variable b has value", b, "and type", type(b))
print("Variable c has value", c, "and type", type(c))
print("Variable d has value", d, "and type", type(d))

# You can reuse variables but it is considered bad form to change the type mid program. 
#
a = 6
print()
print("Variable a has value", a, "and type", type(a))
print("Variable b has value", b, "and type", type(b))
print("Variable c has value", c, "and type", type(c))
print("Variable d has value", d, "and type", type(d)) # notice that this did not change. d = a * c is not an equivalence, but an assignment. 

# Casting 

e = int(c) # int() converts its argument to an integer value. If the argument is a float it truncates it. 
print()
print("Variable e has value", c, "and type", type(c))
print("Variable e has value", e, "and type", type(e))

f = float(a)
print()
print("Variable a has value", a, "and type", type(a))
print("Variable f has value", f, "and type", type(f))

# Casting from numeric to string 

g = str(a)
h = str(c)

print()
print("Variable g has value", g, "and type", type(g))
print("Variable h has value", h, "and type", type(h))

# Casting from numeric to string 

i = input("Enter a number: ")
j = float(i) # this only works if the string represents a valid number

print()
print("Variable i has value", i, "and type", type(i))
print("Variable j has value", j, "and type", type(j))
