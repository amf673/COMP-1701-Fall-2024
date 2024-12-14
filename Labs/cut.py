
#
# 
# L10A cut.py
#

# 

def enter_int(prompt:str) -> int:
    """ prompt until something is entered """
    resp = input(prompt)
    while resp.strip() == "": 
        resp = input(prompt)
    number = int(resp)

    return number


def main() -> None:
    """ cut a column from as file. """
    input_file_name = input("Enter a file name: ")

    left = enter_int("Enter the left bound: ")
    right = enter_int("Enter the right bound: ")

    if left <= 0 or left >= right: 
        
        print("Error: Left must be > 0 and < right")

    else:

        input_file = open(input_file_name, "r")

        line = input_file.readline()
        while line != "":

            output_line = line[left:right]
            
            print(output_line)

            line = input_file.readline()

        input_file.close()


main()



