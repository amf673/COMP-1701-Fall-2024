## Python Techniques That You Cannot Use

Here is a list of the techniques that we have not covered in class, that you are not allowed to use in your labs or assignments. 

The main reason for this is that the outcome of COMP 1701 is introductory programming. We want students to finish the course 
with general programming skills that can transfer to other programming environments. To be a proficient programming you need to 
know how to do basic operations ... working with while loops, working with arrays (lists). 

The techniques described here tend to be of two types. Some are Python specific and we are not really teaching Python, we are learning programming. The other are 
poor programming style that we want to discourage. 

## While True: and break and continue

We have been creating loops that have a loop control variable (LCV), which is tested in some way in the loop condition and then we update the LCV within the loop. 
You will often see loops that look something like this: 

```Python
while True:
   inp = input("Enter something: ")
   if inp == "END":
      break
   else:
      # do something else.
```
There are times when a while True: is the right choice (GUI listeners or TCP listeners) but in this class there is no problem where this should 
be used. It is much like the 'goto' that I was forbidden to use in my intro programming classes, it results in hard to read and understand and debug code. (A code review would expost this.) 
We can now have multiple conditions and multiple points where a loop can end. So while True: in this class. 

## Multiple returns 

Normally a function should only have one return statement. There are times where multiple returns are ok but do try to avoid it. It makes for mulitple conditions and points where the 
function could end, and again hard to read and hard to debug code. 






