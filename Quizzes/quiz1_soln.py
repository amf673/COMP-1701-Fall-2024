## Quiz 1 tracing in Python
##
## COMP 1701
number = int(input("Enter a positive number: "))
result = ""

while number > 0: 
    if (number / 2 - number//2) != 0:
        bit = "1"
    else:
        bit = "0"
    result = bit + result 
    number = number // 2

print(result)
