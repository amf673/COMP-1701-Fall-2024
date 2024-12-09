# 
# a function to create an empty list
# 
def empty_list(n:int, init_value)-> list:
    """ Create an empty list of size n. Intialize the cells to init_value"""
    new_list = []
    for i in range(n):
        new_list.append(init_value)
    return new_list

def empty_2d_list(rows:int, cols:int, init_value) -> list:
    """ Create an empty list of size rows x cols. Intialize the cells to 0."""
    new_list = []
    for i in range(rows):
        new_list.append(empty_list(cols), init_value)
    return new_list

def new_2d_list(rows:int, cols:int, init_value) -> list: 
    """ Create an empty 2d list """
    new_list = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(init_value)
        new_list.append(row)
        
    return new_list
    

def main():
    r = int(input("Enter the number of rows you want: "))
    c = int(input("Enter the number of columns you want: "))
    int_list = empty_2d_list(r,c,0)
    print(int_list)

main()
