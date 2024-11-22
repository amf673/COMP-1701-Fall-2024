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

## ``if __name__ == "__main__"``

This shows up in a lot in examples. It is something that you would use if you were creating a program with various modules and all of our programs are single modules. It does not mess anything up, but it is not usually needed. The if statement checks if this is the module that was called to execute and if it is, it executes main(). If this module was imported the if will not be true and main() will not be executed. 

## List comprehensions 

Another technique that shows up often on Stack Overflow and ChatGPT. A list comprehension is 
a way to create and work with lists. We do not teach them as this is not available in other languages and
it is important to have the skills to do these operations with the tools available.

An example from w3 schools is:
```Python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
```
## Dictionaries, Maps and Tuples

Python provides a number of data structures for working with collections of objects. We use ``list``s. There are also 
- Tuples - like a mathematical tuple. A 4-tuple could be (1,2,5,6)
- Sets - like a mathematical set. No duplicates.
- Dictionaries - a key value store.
We will not be teaching any of these and none of the programming we do needs them.

## try/except 

This is Python's run time error handling mechanism. A similar feature exists in Java. This is something that is covered in the second programming class. We will use try/except for file handling, but not for anything else. 

## Returning multiple values

If is possible in Python to do something like this: 

```Python
def foo (x:int, y:int):
   """ a nonsense function """
   return (x+1, y+1)
```
which in some instances may seem like a good thing to do. Python, like most progamming languages (C++, Java) does not allow returning multiple values. This construct creates a Tuple and returns that.
We are not using Tuples (see above). You code is much more readable, easier to test and maintain when it is kept simpler, so not returning Tuples. 










