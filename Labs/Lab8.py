# 
# 
# L8 
# COMP 1701 
# 
# A. Fedoruk



def enter_str(prompt:str)->str:
    """ Prompt user and return a non-empty string."""

    resp = input(prompt).strip()
    while resp == "":
        resp = input(f"String must be non-empty. {prompt}").strip()

    return resp.strip()


def enter_int(prompt:str) -> int:
    """ Prompt for a int."""

    resp = enter_str(prompt)
    num = int(resp)
    while num < 0: 
        resp = enter_str(prompt)
        num = int(resp)

    return num


def enter_int_range(prompt:str, low:int, high:int)->int:
    """ Prompt for a int."""

    resp = enter_str(prompt)
    num = int(resp)
    while not(num >= low and num <= high): 
        resp = enter_str(prompt)
        num = int(resp)

    return num


def yorn(prompt:str) -> bool: 
    """ Prompt for y or n"""

    resp=input(prompt).strip()
    while not(resp == "y" or resp =="n"):
         resp=input(prompt).strip()

    return resp == "y"
    
def count_up( bound:int) -> str:
    """ Count up from 0 to bound and return a string """

    count_str = ""
    for i in range(0, bound+1):
        if count_str == "": 
            count_str = "0"
        else:
            count_str = count_str + "," + str(i)

    return count_str


def count_between( l:int, u:int) -> str:
    """ Return a string of numbers between l and u """

    count_str = ""
    for i in range(l+1, u+1):
        if count_str == "": 
            count_str = "0"
        else:
            count_str = count_str + "," + str(i)

    return count_str


def string_between(low:str, high:str) -> str:
    """ Return the characters between low and high """

    l = ord(low)
    h = ord(high)
    result =""
    for i in range(l+1, h):
        if i % 2 == 0:
            result = result + chr(i).upper()
        else:
            result = result + chr(i).lower()

    return result

    
def main():

    print( enter_str("Enter a string: "))

    print( enter_int("Enter a non zero int: "))

main()

