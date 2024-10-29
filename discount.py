# 
# Grocery Store Discount 
# 

GST = 0.05
DISCOUNT = 0.15 

def adjusted_total( is_first_tuesday:bool, total:float) -> None:
    """ Calculate the total owing. If it is the first Tuesday
     and the total is more than $50, give the discount. """

    if is_first_tuesday and (total > 50): 
        total = total * (1.0 - DISCOUNT)
        print("Congratulations, you qualify for the discount!")

    total_with_tax = total * (1.0 + GST) 
    
    print(f"Your total with tax is ${total_with_tax:.2f}")

def main()->None:
    # Some testing. Test all combos. 
    adjusted_total(False, 25.0)
    adjusted_total(True, 25.0)
    adjusted_total(False, 75)
    adjusted_total(True, 75.00)
    adjusted_total(True, 50.00)
    adjusted_total(True, -1)

main()
