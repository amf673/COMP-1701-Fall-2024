# Quiz 5 - Question 1 Tracing

def foo(n:int, m:int)->None:
    """ foo is foo """
    i = n
    while i >= m: 
        if i < 0:
            diff = "Plus"
        else:
            diff = "Minus"
        print( f"T-{diff} {abs(i)} seconds.") 
        i = i - 1

def main()->None:
    foo(5,-5)

main()

