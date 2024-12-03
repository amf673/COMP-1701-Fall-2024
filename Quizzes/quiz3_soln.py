# Quiz 2 programming question

# Write a Python function, continue(prompt:str)->bool that asks the user 
# to enter “y” or “n”, using prompt in the input() function call. 
# Return True if the user enters “y”, False otherwise.

# The purpose of this question is to have you demonstrate that you can 1) write a complete
# function and 2) can use booleans and have a function return a boolean value. 

# Here is version 1. 
def cont1(prompt:str)->bool:
    """ prompt the user for y or n and return True if they 
    answer y"""
    # get the response from the user. Note the use of the variable `prompt`
    response = input(prompt)

    if response == "y": 
        return True
    else:
        return False

# Here is another, simpler version. 

def cont2(prompt:str)->bool:
    """ prompt the user for y or n and return True if they 
    answer y"""

    response = input(prompt)
    return response == "y"
    # 
    # We need a boolean that is True or False if response is "y" or something else. 
    # 
    # response == "y" 
    # 
    # is an expression that evaluates to True when response has the value "y", False otherwise. 
    # 
    # We can simply return that... 
    
# Finally, we can make it a one liner!
def cont3(prompt:str)->bool:
    """prompt the user for y or n and return True if they answer y"""
    return input(prompt) == "y"

def main()-> None:
    if cont1("Do you want to continue? "):
        print("Go on")
    if cont2("Do you want to continue? "):
        print("Go on")
    if cont3("Do you want to continue? "):
        print("Go on")

main()
