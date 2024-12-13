##
# Lab 11 Times Table Redux
#
# 

def tt_row(r:int, n:int)->list:
    """ Return the ith row for a times table of 
    size n"""
    
    row = []
    for i in range(1,n+1):
        row.append(i*r)
    
    return row


def times_table(n:int)->list:
    """ return a times table of size n"""

    tt = []
    for i in range(1,n+1):
        tt.append(tt_row(i,n))
    
    return tt

def tt_lookup(tt:list, i:int, j:int) -> int:
    """ Lookup the value for i * j """

    return tt[i-1][j-1]


def main():
    n = int(input("Enter times table size: "))
    tt = times_table(n)
    print(tt)

    i = int(input("Enter i: "))
    j = int(input("Enter j: "))
    print( tt_lookup(tt,i,j))

main()