#
# Caffeine Example 
# 

def caff1(caffeine:int)->None:
    """ Prints a message depending on the caffeine levels. 
    Incorrect Version!
    """
    if caffeine >50 :
        print("Good start")
    elif caffeine > 100:
        print("Perfect amount")
    elif caffeine > 200:
        print("TOO MUCH!")
    else:
        print("You need more!")

def caff2(caffeine:int)->None:
    """ Prints a message depending on the caffeine levels. """
    if caffeine >50 :
        print("Good start")
    elif caffeine > 100:
        print("Perfect amount")
    elif caffeine > 200:
        print("TOO MUCH!")
    else:
        print("You need more!")

def main()->None:
    # Testing. 
    # Try one for each category and boundaries. 
    print("Caffeine = 0")
    caff2(0)
    print("Caffeine = 50")
    caff2(50)
    print("Caffeine = 75")
    caff2(75)
    print("Caffeine = 100")
    caff2(100)
    print("Caffeine = 150")
    caff2(150)
    print("Caffeine = 200")
    caff2(200)
    print("Caffeine = 300")
    caff2(300)

    ## try the other one 

    print("\n\nUsing the other version\nCaffeine=400")
    caff1(400)

main()
