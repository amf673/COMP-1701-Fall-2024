# Q5 Q2. 
# Write a while loop that is equivalent to this for loop.  

""" n = 10
sum = 0
for i in range(0,n,2): 
    sum = sum + i**3
print(sum) """


""" For this one we want to understand what the for loop is doing. 

- It has a loop control variable of i. 
- i is initialized to 0. 
- the loop continues until i is greater than n, which is 10. 
- i is updated by adding two each loop. 

So we get this code:  """

n = 10 
sum = 0 
i = 0 
while i < n:  
    sum = sum + i**3 
    i = i + 2 
print(sum) 
