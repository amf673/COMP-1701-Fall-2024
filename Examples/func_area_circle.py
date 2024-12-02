# 
# Author Information
# 
# A. Fedoruk
# Jan 2024, COMP 1701 

# This program is a sample of the typical structure for a Python program. 
#

# Import any required modules

import math 

# Define constants 

PI = math.pi
SUPERSCRIPT2 = "\u00B2"

# Function definitions 

def area_circle(radius: float) -> float: 
    """ Return the area of a circle of the given radius"""
    return PI * math.pow(radius,2)

# Main function definition 

def main():
    # input 
    
    radius = float(input("Enter the Radius in meters: "))

    area = area_circle(radius)

    print(f"The area of a circle of {radius:.2f} m is {area:.2f} m{SUPERSCRIPT2}")

# invoke main()
main()
