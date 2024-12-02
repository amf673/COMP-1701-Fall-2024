# 
# Area of a polygon 
# 
# COMP 1701 
# 
# A. Fedoruk
#

import math

def area_polygon( sides:int, apothem:float)-> float: 
    """Return the area of a 'sides' sided polygon with the given apothem."""
    area = apothem * apothem * sides * math.tan( math.radians(180/sides))
    return area


def main()->None:
    n = int(input("Number of sides: "))
    ap = float(input("Apothem Length: "))
    ap = float(input("Apothem Length: "))

    print(f"A polygon with {n} sides and apothem length of {ap:.2f} has area {area_polygon(n,ap):.2f}")

main()
