## 
## Quiz 6 solution
## 

def foo(n: int) -> list:
    """ Builds a list and returns it """
    a_list = []
    for num in range(1, n + 1):
        # We are appending n -- which does not change! as a string to the list. 
        a_list.append( str(n))
    return a_list

def skip(a:str, n:int)->str:
    """ skip using a list """
    new_a = ""
    for i in range(len(a)):
        if i % n == 0: 
            new_a = new_a + a[i]
    return new_a

def skip1(a:str, n:int)->str:
    """ skip using string slicing """
    return a[0:len(a):n]


def main():
    print("\n\nQ1\n----------")
    
    # See foo()
    a = foo(4)
    print(a) 
    
    print("\n\nQ2\n----------")

    # Changing word does not change the list so word_list will be unchanged. 

    word_list = ["MOOSE", "SQUIRREL"]
    for word in word_list:
        word = word.lower()
    print(word_list)

    print("\n\nQ3\n----------")

    print(skip("capybara",3))
    print(skip1("capybara",3))

    print(skip("cat",2))
    print(skip1("cat",2))

main()
