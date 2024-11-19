"""
create a function that takes str, returns a str 
in sarcastic font. 

Algorithm: 

    loop through the string, one character at a time. 
    - convert to upper or lower 
    - add that char to our result string. 

    return new string

Need string slicing for this. Try these to see what they do.

    a = "comp1701_is_fun!"

    print(a[10])
    print(a[0:5])
    print(a[5:])
    print(a[5:len(a)-2])
    print(a[:7])
"""

def sarc2(s:str)->str:
    upper = True
    result = ""
    for ch in s:
        if  upper:
            result = result + ch.upper()
        else: 
            result = result + ch.lower()
        upper = not upper
    return result


def sarc(s:str)->str:
    upper = True
    result = ""
    for i in range(0, len(s)):
        if  upper:
            result = result + s[i].upper()
        else: 
            result = result + s[i].lower()
        upper = not upper
    return result

def sarcastic(sentence:str)->str: 
    """ convert to sarcastic. """
    i = 0
    upper = True
    result = ""
    while i < len(sentence):
        ch = sentence[i]
        if  upper:
            result = result + ch.upper()
        else: 
            result = result + ch.lower()
        upper = not upper
        i = i + 1
    return result

def main()->None:
    s = input("Enter a sentence: ")
    print( sarc2(s))

main()
