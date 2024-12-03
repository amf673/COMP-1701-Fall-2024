# Quiz 4 question 1
# Tracing 
def foo ( x : int ) -> int:
  """ foo docstring """
  x = x * 2
  return x

def bar ( x : int ) -> int:
  """ bar docstring """
  y = foo ( x * 2)
  return y

def main ()-> None :
  print ( bar (5))
  print ( foo (5))

main ()
