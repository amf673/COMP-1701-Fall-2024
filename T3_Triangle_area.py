# A sample for Tutorial 4 
# 

import math

def semi_peri( a:float, b:float, c:float) -> float:
    """ Calculate the semi-perimeter of a triangle with sides a,b,c"""
    return (a + b + c) / 2

def area_triangle(a:float, b:float, c:float) -> float:
    """ Calculate the area of a triangle with sides a,b,c using
        Heron's formula."""
    s = semi_peri(a,b,c)
    area = math.sqrt( s * (s-a) * (s-b) * (s-c))
    return area

def main() -> None:
    a = float(input("Enter first side of triangle: "))
    b = float(input("Enter second side of triangle: "))
    c = float(input("Enter third side of triangle: "))
    print( f"The area of the triangle is {area_triangle(a,b,c):.4f}")
          
main()
