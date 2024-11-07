# 
# Fibonacci Numbers: https://en.wikipedia.org/wiki/Fibonacci_sequence
# 
def fib_1 (n:int)->None:
    """ print the first n Fibonacci numbers """
    if n == 0: 
        print("0")
    elif n == 1:
        print("0, 1")
    else:
        print("0, 1", end="")
        nminus1 = 1
        nminus2 = 0
        for i in range(2,n):
            curr = nminus1 + nminus2
            print( f", {curr}", end="")
            nminus2 = nminus1 
            nminus1 = curr
        print()

def main():
  fib_1(50)

main()
