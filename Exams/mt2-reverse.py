# Tracing question
# 

def f(x:int) -> int:
    y = 0
    while x > 0:
        y = (y * 10) + (x % 10)
        x = x // 10
    return y

def main()->None:
   print(f(543))

main()
