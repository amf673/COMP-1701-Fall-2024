# 
# The guessing game
# 

RANGE_LOW = 1
RANGE_HIGH = 10 

import random

def get_number(a:int, b:int)-> int: 
    """ Return a random int between a and b"""
    return random.randint(a, b)

def get_user_number(a:int, b:int)->int:
    """ Prompt the use for a number between a and b inclusive."""
    return int(input(f"Enter a number between {a} and {b}: "))

def main()->None:
    # Get the computers number
    n = get_number(RANGE_LOW, RANGE_HIGH)

    # Get the users first guess
    user_n = get_user_number(RANGE_LOW, RANGE_HIGH)
    # As long as the users guess is wrong ... 
    while not(n == user_n): 
        if n < user_n:
            print("Too high!")
        else:
            print("Too low!")
        # Get the next guess
        user_n = get_user_number(RANGE_LOW, RANGE_HIGH)
    print("Got it!")

main()
