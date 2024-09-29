# 
# COMP 1701 Fall 2024
# 
# Assignment 1 Tracing 
# 
# A. Fedoruk 
# 
# Estimate the value of pi

import math

number = int(input("Enter a number: "))
             
counter = 1
result = math.sqrt(12)
print(f"counter = {counter:4d} term =            result = {result:10.6f}" )

while counter < number: 

    numerator = math.sqrt(12)

    a = (-3)**counter
    b = 2 * counter + 1
    denominator = a * b 

    term = numerator / denominator
    result = result + term
    counter = counter + 1
    print(f"counter = {counter:4d} term = {term:10.6f} result = {result:10.6f}" )

print( f"\n\nFinal Result    = {result:30.19f}")

print( f"\n\nThe value of pi = {math.pi:30.19f}")

print( f"\n\nThe difference  = {result-math.pi:30.19f}\n\n\n")
