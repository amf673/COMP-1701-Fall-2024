# COMP 1701 
# Fall 2024
# Lab 4

import math

OVEN_TEMP_CONST = 350
CCS_CONSTANT    = 20
BASE_CAKE_SIZE  = 6
PI = math.pi

def round_n( i:int, n:int) -> int:
    """Rounds i to the nearest n"""
    return int(round(i/n)*n)

def round_5( n:int) -> int:
    """Rounds the integer argument to the nearest 5."""
    return round_n(n,5)

def area( radius:float) -> float: 
    """ return the area of a circle of the 
    given radius. """
    return PI * radius * radius

def area_diameter( diameter:float) -> float:
    """ return the area of a circle with diameter given """
    return area( diameter / 2)

def cake_time( temperature:int, diameter:float) -> float: 
    """ return the baking time for a cake of size diameter and oven temp temperature"""

    time = CCS_CONSTANT + (OVEN_TEMP_CONST * (area(diameter) - area(BASE_CAKE_SIZE))) / (2 * temperature)
    
    # round the result of from above to the nearest 5 minutes.
    return round_5(time)

def main():

    temperature = int( input( "Enter the temp in F: "))
    cake_size = float( input( "Enter the size of the cake in inches (6-12): "))

    bake_time = cake_time( temperature, cake_size)
    
    print(f"Your cake should take about {bake_time} minutes to bake.")

def testing():
    """ Does some testing of a variety of cases. """
    temp = 350.0
    cake_size = 6.0
    expect = 20.0
    bake_time = cake_time 
    print(f"expected - calculated = {expect-bake_time(temp, cake_size)}")

    temp = 350.0
    cake_size = 10.0
    expect = 45.0
    bake_time = cake_time 
    print(f"expected - calculated = {expect-bake_time(temp, cake_size)}")

    temp = 400.0
    cake_size = 11.5
    expect = 55.0
    bake_time = cake_time 
    print(f"expected - calculated = {expect-bake_time(temp, cake_size)}")

    temp = 400.0
    cake_size = 8.5
    expect = 30.0
    bake_time = cake_time 
    print(f"expected - calculated = {expect-bake_time(temp, cake_size)}")

    print(area(1), area_diameter(2), area(4))
    print( round_n(22,5))
    print( round_n(24,5))
    print( round_5(23))
    print( round_5(41))
# main()
testing()
