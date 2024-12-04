# 
# Fibnonaci Numbers
# 

def fib(n:int)->int:
    """ return the nth Fibbonacci number """
    num = 0
    if n == 0 or n == 1: 
        num = n
    else: 
        num = fib(n-1) + fib(n-2)
    return num

def main(n:int)->None:

    print(fib(n))

main(12)
        
