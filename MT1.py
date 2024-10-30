# COMP 1701 MT 1 Coding Question B
#
# 

GST = 0.05 

def main() -> None: # one for main()

    # 3 for inputs 
    purchase_price = float(input("Enter the purchase price of your item: "))
    number_of_items = int(input("Enter the number of items: "))
    discount = int(input("Enter the discount amount (0-100): "))

    # 4 for calc
    total_price = number_of_items * purchase_price
    discount_price = total_price - discount
    gst_amount = discount_price * GST 
    final_total = total_price + gst_amount
    # 6 for output
    print(f"Purchase of {number_of_items} items @ ${purchase_price:.2f} each equals ${total_price:.2f}")
    print(f"With the discount of ${discount} the total is ${discount_price:.2f}")
    print(f"The total for the sale is ${discount_price:.2f} plus ${gst_amount:.2f} GST equals ${final_total:.2f}")

main()
