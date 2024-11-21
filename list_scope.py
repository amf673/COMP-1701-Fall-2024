## Lists and scope 
## pass by reference and pass by value

def foo( a_list:list, x:int) -> None:
    """ A useless function to show the difference between lists 
    and other variables. 
    The list a_list is passed 'by reference', the reference to the calling object is 
    given to the function. When you change it in the function it is changed in the calling function as well. 
    
    The variable x, an int is passed 'by value' -- only the value is given to the function, so when you 
    change it in the function, it is not changed in the calling function. 
    """
    if len(a_list) >= 1: 
        a_list[0] = x
    x = 199999

def bar( a_str:str) -> None:
    """ Another useless function that shows that strings 
    are passed by value. 
    """
    a_str = "HELLO"

def main()->None:
    """ Test the functions to demonstrate pass by value and pass by reference. """
    
    a = [2,3,4]
    x = 88
    foo( a, x) 
    print(a)
    print(x)

    c = "GOODBYE"
    bar(c)
    print(c)

main()
