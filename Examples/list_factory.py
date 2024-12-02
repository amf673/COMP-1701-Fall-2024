# 
# a function to create an empty list
# 
def empty_list(n:int)-> list:
    """ Create an empty list of size n. Intialize the cells to 0."""
    new_list = []
    for i in range(n):
        new_list.append(0)
    return new_list

def empty_2d_list(rows:int, cols:int) -> list:
    """ Create an empty list of size rows x cols. Intialize the cells to 0."""
    new_list = []
    for i in range(rows):
        new_list.append(empty_list(cols))
    return new_list

def main():
    r = int(input("Enter the number of rows you want: "))
    c = int(input("Enter the number of columns you want: "))
    int_list = empty_2d_list(r,c)
    print(int_list)

main()
