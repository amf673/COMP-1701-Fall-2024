
#--------------------------------------------------
## Example 1. A counted while loop. 

i = 0        # this is the loop control variable 
limit = 10

while i < 10:   
    ## the condition has i in it. This says keep looping as long
    ## i is less than 10 
    print(i)
    i = i + 1 ## update the loop control variable. Without this infinite loop. 

#--------------------------------------------------
## Example 2. A counted loop with increment 2. 

i = 0        # this is the loop control variable 
limit = 10
increment = 3

while i < 10:   
    ## the condition has i in it. This says keep looping as long
    ## i is less than 10 
    print(i)
    i = i + increment ## update the loop control variable. Without this infinite loop. 

#--------------------------------------------------
## Example 3. A counted loop that is counting down. 

i = 20        # this is the loop control variable 
limit = 0
increment = -1

while i > limit:   
    ## the condition has i in it. This says keep looping as long
    ## i is less than 10 
    print(i)
    i = i + increment # update the loop control variable. Without this infinite loop. 

#--------------------------------------------------
## Example 4. A sentinel loop. 

response = input("Enter a number, or <enter> to end: ") 
## response is the loop control variable. This is known as a 
## priming read. 

while response != "": 
    ## loop until response is an empty string
    ## OR loop as long as the use enters something. 
    num = int(response)
    print(num)
    ## The loop control variable MUST be updated in the loop
    ## so we do that here. 
    response = input("Enter a number, or <enter> to end: ")

#--------------------------------------------------
## Example 5. A counted loop with an accumulator

i = 0        # this is the loop control variable 
limit = 10
sum = 0      # this is the accumulator. We intialize it to 0

while i < 10:   
    # the condition has i in it. 
    # This says keep looping as long
    # i is less than 10 
    print(i)
    sum = sum + i
    i = i + 1 ## update the loop control variable. Without this infinite loop. 

print(sum)

#--------------------------------------------------
## Example 6. A sentinel loop with an accumulator 

response = input("Enter a number, or <enter> to end: ") # priming read. 
sum = 0 # intialize accumulator

while response != "": 
    ## loop until response is an empty string
    num = int(response)
    print(num)
    sum = sum + num
    ## The loop control variable MUST be updated in the loop
    ## so we do that here. 
    response = input("Enter a number, or <enter> to end: ")

print(sum)
