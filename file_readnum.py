# 
# In this example we read a file that has a single integer 
# on each line and compute the sum of all the integers. 
# Additional we keep track of how many numbers there were and calculate 
# the average. 
# 
input_file = open("nums.txt", "r")
i = 0
sum = 0 

line = input_file.readline()    
while line != "":          
    i = i + 1
    sum = sum + int(line)
    line = input_file.readline()

input_file.close()

print(f"The sum of {i} integers is {sum}")
if i != 0: 
    print(f"The average is {sum/i:.2f}")

