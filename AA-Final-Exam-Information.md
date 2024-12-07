# Final Exam Information

## COMP 1701 Fall 2024

## Date and Time
Monday Dec 16, 2024 3:00 p.m. to 6:00 p.m.(3 hours)
U170 (Gym) Row 27 (seat 11 and up) to Row 29. 

## What to bring

- Writing implements and spares.
- 1 8 1/2 x 11-inch sheet of notes. Both sides can be written on and it can be hand-written or computer printed.
- A simple calculator.
- Something to drink. I am not worried about whether or not the bottle is clear or not, just don't bring a bottle that plays music or something when you drink from it.

Phones, laptops or other electronics (except a simple calculator) are not allowed. 
You can leave all of your belongings on the tables at the front (or back depending on your perspective) of the gym. 
You will likely get an email from the registrar's office with a bunch of rules about when you can arrive etc. 

## Format of the Exam

- 14 multiple choice 14 marks/19%. 
- 4 short answer/tracing 17 marks/23% 
- 5 coding 45 marks/60%

The exam will be much like the two midterms in character. 

## What to Study

The exam is comprehensive, meaning material from the whole semester will be on the test.
Lecture notes, labs, tutorials, assignments, quizzes, and midterms are all valuable study materials. 
If anything is missing from the D2L site or the github repository (https://github.com/amf673/COMP-1701-Fall-2024), 
let me know. 

## What to Do During the Exam

- Strive to get there on time. I suggest arriving at least 15 minutes early, you want to be settled in and relaxed when the exam starts.
- You do not need to have your One Card on the desk but you should probably have it with you. 
- I will pass around a sign-in sheet. This is something the department asks for and is a nice double-check to make sure I don't miss an exam.
- When you are finished, bring your paper up to me.  I will check that your name is on it, etc., check you off my list and add it to the pile. Then you are free!
- The end of three hours (6:00 p.m.) is a hard stop. I will collect all the papers at that time.
- I have included some extra pages at the end of the exam for rough work or if you need more space. If it is easier to unstaple the exam booklet to work, do so. We can restaple.
- To aid in grading, please clearly indicate what is rough work or first draft and what is the work you would like graded.
- If you have questions, raise your hand and I will come to you.
- If you need to go to the washroom, raise your hand. Normally only one person is permitted out of the room at a time. 

I will have with me:

- Extra pencils and pens.
- Extra exams.
- Extra paper.
- A stapler.

## Advice

This was designed to be a two-hour exam and we have three hours to do it. 

When the exam starts, I suggest reading through the whole thing. 
It will only take a few minutes and it will give you a better idea of how to budget your time. 

If you are not getting a question, move on. You can come back to it later. 

The multiple-choice questions are meant to be done fairly quickly. They are only worth 1 each. The final will be out of about 75, and the exam is weighted at 30% so each multiple-choice is worth 0.4 of your final grade. 

The coding questions all have solutions that are less than 20-30 lines. If your code is getting long, you are likely off track and should rethink what you are doing. 

Three hours is a long time to sit with a pen cramped in your hand. Put the pen down now and then, stretch out your arms, and take a few breaths. 

I know that final exams are stressful. I had a stomach ache all of December and April for 5 years when I was an undergrad, back in the 1980s. 
I think the most important thing I learned from that was to get a good night's rest the day before.  
Extra studying will help, but extra sleep helps even more. 

## Coding Do's and Don'ts for the Final Exam

Coding on paper is a bit different than coding on the machine with VS-Code. 
But, just like live coding you need to have a plan (the algorithm) either written down or in your mind before you start coding. 
Lots of scrap paper will be available. 
Sketching out the algorithm BEFORE writing the code is very, very helpful to getting a correct soltution. 

Your code will not be perfect, but what we are looking for when we are marking paper code is: 

- Is the algorithm correct? Would this code solve the problem at hand? 
- Is it valid Python? Perfect syntax is not required but it should clearly be Python code and not something else. 

### Things To Do

#### 1. Read the questions carefully. 

You need to fully understand what is being asked before you can write a line of code. 
Some questions ask you to write a function so you only need to write that. Others ask for a complete program 
which should include a ``main()`` function and a call to ``main()``. 

#### 2. Include type hints for all of your parameters and return values. 

```Python
    def my_awesomefunction( x:int, y:float) -> float:
    
    def my_other_function(applicant:list) -> None:
```

#### 3. Use appropriate names for all variables and functions. 

The goals is to have variable names that tell the reader what the variable is storing. 
Longer is not always better. ``i`` is a perfectly good name for a variable used as a loop counter. 
Name your variables for what they represent. 

```Python
    applicant = [] # a list a values that represents an applicant to the skilled worker program
    applicants = [] # a list of applicants, each value is a list that represents an applicant.
```

Functions usually do something, like ``print()`` or ``input()`` so name them for the action they perform. 

```Python
    def count_neighbours(life_grid:list)->int
```

#### 4. Include a docstring for every function. 

This can be quite succcinct, a line or two, and should describe what the function does.

```Python
def count_neighbours(life_grid:list, row:int, col:int)->int:
    """ Count the number of neighhours for cell life_grid[row][col] according to the Game of Life rules.
        Returns an int from 0 to 8. 
    """
``` 

Even if your function is not coded correctly, having a correct docstring will gain marks. 

### Things Not To Do

#### 1. Don't Create Infinite Loops

```Python
while True: 
    # ... 
    # ... 

```

There is a time and place to use this type of loop and it is not during this class.  Gui processing and and other real time event handling can need a ``while True`` but nothing we will ask in this class would require it. 
You need to figure out what your loop continue condition is and code that. 

Think about what is your loop control variable? How is it initialized? How is it updated? What is the loop end condition? 

#### 2. Don't Compare boolean variables to boolean literals

```Python
if a_bool == True: 
    # 
elif b_bool == False: 
    # 
else 
    #
```

This is redundant. A boolean variable evaluates to a boolean so you can use it directly. 

```Python
if a_bool: 
    # 
elif not b_bool: 
    # 
else 
    #
```
Similarly, you do not need to do: 

```Python
if response == "y":
   return True
else:
   return False
```
You can just do: 
```Python
return response == "y"
```

#### 3. Don't Use Multiple return statements. 

Generally a function should have one return statement. There are times when more would be OK, but strive for one. 

```Python
def score_age(applicant:list)->int: 
    """ Calculate the score for the age category for this applicant. 
    """
    if age < 18: 
        points = 0
    elif age <= 35:
        points = 12
    else 
        points = min(47-age,0)

    return points
```

#### 4. Don't Use List Comprehensions

You may have found these online and they can be useful but there is nothing that we are asking you to do that would require one. List comprehensions look like this: 

```Python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
```

Whatever they do can always be done with a while loop. And most other languages (like Java in COMP 1502 or C++ in COMP 1633) do not have the feature so it is necessary to learn to do this without them. 

#### 5. Don't Use try/except 

This is an important piece of programming but beyond the scope of this class. You will learn about this construct in you next programming class. 

#### 6. Don't Use List sum()

Constructs like this: 
```Python
    sum([x ** 2 for x in range(1, 6)])
```

are a very Python way to do things, but you can always do it using while loops and that is what you will have to do in other environments, so we want you to learn the loop algorithms rather than use this shortcut. 

#### 7. Don't Use Any of the other collections types in Python. 

We used lists but Python also has ``sets``, ``tuples`` and ``dictionaries``. We only worked with lists, so the others are off limits. 

#### 8. Don't Use map() 

We have not covered using map(). These is an element of functional programming that gets covered in upper year classes. 
