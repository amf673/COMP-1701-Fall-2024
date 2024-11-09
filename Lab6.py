#
# COMP 1701 
# Winter 2024
# 
# Lab 6
# A. Fedoruk

FREE_DELIVERY_LIMIT = 35
DISTANCE_LIMIT = 15

def check_free_delivery(amount: float) -> str:
    """
    Takes the total amount of the order and checks
    whether the order qualifies for free delivery.
    returns a string message.
    """    
    if amount < 0: 
        message = "Invalid entry, orders must be positive"
    elif amount < FREE_DELIVERY_LIMIT: 
        message = f"Add ${FREE_DELIVERY_LIMIT - amount:.2f} to your order to get free delivery"
    else: 
        message = "You get free delivery!"

    return message

def check_free_delivery_bonus(distance:float, order_amount:float) -> str:
    """ Takes the distance of the delivery and if it is in range, 
    check the total amount of the order and checks
    whether the order qualifies for free delivery.
    returns a string message.
    """    

    if distance < 0: 
        message = "Invalid entry, distance must be positive"
    elif distance <= DISTANCE_LIMIT:
        message = check_free_delivery(order_amount)
    else:
        message = "Sorry, you are not eligibile for free delivery"
    return message

def main_bonus() -> None:
    """
    Prompts the user for the distance and total amount of the order and calls
    check_free_delivery_bonus with the user's input.
    Prints an appropriate message based on whether the order qualifies
    for free delivery.
    """

    order_price = float(input("What is the dollar amount of the current order? "))
    delivery_distance = float(input("Enter the delivery distance in km: "))
    msg = check_free_delivery_bonus(delivery_distance, order_price)
    print(msg)


def main() -> None:
    """
    Prompts the user for the total amount of the order and calls
    check_free_delivery with the user's input.
    Prints an appropriate message based on whether the order qualifies
    for free delivery.
    """

    order_price = float(input("What is the dollar amount of the current order? "))
    msg = check_free_delivery(order_price)
    print(msg)

main()
