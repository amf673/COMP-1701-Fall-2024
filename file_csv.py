 
# Example of reading a csv file
#
# 

READ_MODE = "r"
WRITE_MODE = "w"
APPEND_MODE = "a" 

csv_file = open("animals.csv","r")

header = csv_file.readline()
# we will treat the header separately 

line = csv_file.readline()
while line != "":
    # turn the line into a list using split with "." as the separator

    print( line, line.split(",")) 
    line = csv_file.readline()

csv_file.close()
