#
# COMP 1701 Winter 2024
# 
# Lab 6 part 2 
# A. Fedoruk
# 

import math

LOWEST_NUMBER = -math.inf

def largest2() -> int: 
    """ Enter integers until an empty string is encountered and then return the largest integer."""
    
    # intialize the largest number to the lowest possible. 
    largest = LOWEST_NUMBER

    # Read the fist integer, as a string so that we can enter an empty string. 
    user_response = input("Enter an integer, <Enter> to stop: ") # user_response is our LCV
    while user_response != "": 
        # Now convert the string to a number 
        number = int(user_response)
        if number > largest: # We have found a new largest number
            largest = number
        user_response = input("Enter an integer, <Enter> to stop: ") # Update the LCV with an internal read

    return largest

def largest() -> int: 
    """ Enter integers until an empty string is encountered and then return the largest integer."""

    # Read the fist integer and set largest to that. 
    user_response = input("Enter an integer, <Enter> to stop: ") # user_response is our LCV
    number = int(user_response)
    largest = number 
    
    user_response = input("Enter an integer, <Enter> to stop: ") # user_response is our LCV
    while user_response != "": 
        # Now convert the string to a number 
        number = int(user_response)
        if number > largest: # We have found a new largest number
            largest = number
        user_response = input("Enter an integer, <Enter> to stop: ") # Update the LCV with an internal read

    return largest


def main():

    largest_number = largest()
    if largest_number == LOWEST_NUMBER: 
        print("No numbers entered")
    else:
        print(f"The largest number is {largest_number}.")


main()
