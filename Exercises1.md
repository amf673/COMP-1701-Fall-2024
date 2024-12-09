## COMP 1701 

# Programming Problems

## 1. Using print and f-strings

1. In VS-Code, open a new Python file. Call it `E1.py`. 

2. Add a header comment (each line starts with a #) at the top of the file with your name and one line saying what this program is. 

3. Consider this poem

	```None

	Algorithm first
	Data and code and struggle 
	Program emerges
	```

4. Write Python code to print the poem exactly as it is appears above. Include the blank line that precedes the first line. 

5. Write more Python code to print it with a single `print()` statement.

5. Assuming that the output page is 40 characters wide write Python code to print the poem left aligned using f-strings.

6. Assuming that the page is 40 characters wide write Python code to print the poem centered.

7. Assuming that the page is 40 characters wide write Python code to print the poem right aligned.



## 2. Using input and variables

1. In VS-Code, open a new Python file. Call it `E2.py`. and add the required header comment block.

2. Create three string variables, `line1`, `line2`, `line3` and assign the lines from the poem in Exercise 1 to each variable in turn. 

3. Print the poem centered in the 40 character field, as in E1-6. above but using the variables you just created. 

4. Rewrite the code that creates the three variables so that each one is input by the user. Print the poem after the lines have been input. 

5. Run the program so that it prints the three line poem. I encourage you to compose your own poem, and it does not have to be about coding! The scheme is that the first line had 5 syllables, the second 7, and the last line 5 syllables. 


## 3. Input, output and arithmetic expressions 1

1. In VS-Code, open a new Python file. Call it `E3.py`. and add the required header comment block.

2. Write a program that prompts the user for a number of seconds. Remember that `input()` returns a string so the return value from your input statement will need to be ***cast*** to an ``int``. Print the number of seconds.
> **_NOTE:_**  Remember to use meaningful variable names for each variable you create. To complete this exercise you will need 3 variables and it should be clear what values they represent by their names. 

3. Edit the program to calucate the number of minutes contained in the seconds given. This should be an integer value. (Remember the operators that are available to you: +, -, *, /, //, %, **). Print both the number of minutes and the original number of seconds.
> **_NOTE:_** You should always be using f-strings for your output. Even if you don't think you strictly need them, use them to get in the habit. 

4. Run your program multiple times to test it. Use values that you know what the result should be. For example:
   - 0 should calculate 0 minutes.
   - 60 should calculate 1 minute.
   - 240 should calculate 4 minutes.
    - 200 should calculate 3 minutes.

5. How many seconds are remaining after you take out the whole number of minutes? For example, if 100 is entered, that is 1 minute (60 seconds) with 40 seconds left over. Add code to calculate and print that value. Your output should now be three values, the original number of seconds, the minutes and the remaining seconds. Test your code.

6. Did you use a magic number in your code? You needed to divide by the numnber of seconds per minute, 60 That is a good use case for a **named constant**. Remember that constants are all upper case and appear at the top of the program file, after the initial header comment. Add a constant to your code and alter your calculations to make use of it. 

7. Format the output so that it appears like this: ``140 seconds is 02:20`` or  ``65 seconds is 01:05``. Note the leading zeros. You will need to use f-strings to format this correctly. 


## 4. Input, output and arithmetic expressions 2

1. In VS-Code, open a new Python file. Call it `E4.py`. and add the required header comment block. 

2. Building on what you wrote in 3. above write a program that inputs a number of seconds and displays the days, hours, minutes and seconds like this:

``172000 seconds is 1 days 23:46:40``

3. Before you start coding sketch out the algorithm for how you will do this.

4. You will need additional constants to carry out the calculations. 

5. Test your program thoroughly. Here are three, you should test more!
   - 0 should print: 0 seconds is 0 days 00:00:00
   - 60 should print: 60 seconds is 0 days 00:01:00
   - 172000 should print: 172000 seconds is 1 days 23:46:40


## 5. Input, output and arithmetic expressions 3

1. In VS-Code, open a new Python file. Call it `E5.py`. and add the required header comment block.

2. Write a program that prompts for a purchase price, calculates the 5% GST and prints a receipt like this:

```None
   Item Cost $854,269.23
         GST  $42,713.46
   ---------------------

       Total $896,982.69 
```

3. Your program should have three distinct sections: an input section, a processing section and an output section. Don't mix things up. Do all the input, then all the processing, then all output. 

4. Getting the formatting exactly as shown will require some creative use of f-strings. Hint: You can prepare a string that is then printed with the f-string. Strive to have your output be ***exactly*** the same as the sample. 

5. Test your program with a variety of inputs. Try 0. Try small amounts and larger amounts. What is the largest that the formatting works for? 


## 6. Input, output and arithmetic expressions 4

1. In VS-Code, open a new Python file. Call it `E6.py`. and add the required header comment block.

2. Write a program that prompts for an initial investment value, the annual interest rate and the number of years to hold the investment. (When something like an interest rate or growth rate is expressed as a rate, assume a decimal number 0-1.0. If it asked for the percentage then give the rate times 100. i.e. 0.05 is the annual interest rate, which is 5 percent.)

3. Add code to calculate the interest earned based on simple interest and compound interest. The formula for simple interest is $p = p_0 + (p_0 \times r \times t)$ and for compound interest it is $p = p_0 ( 1 + r ) ^t$. For both formulas, $p$ is the final value $p_0$ is the initial value, $r$ is the annual interest rate and $t$ is the number of years.

4. Add code to print the results like this

```None
$1,000.00 invested at 5.00 for 5.5 years will yield:
         $1,275.00 with simple interest.
         $1,307.80 with compound interest, a difference of $32.80.
```

5. Again you will have three distinct sections in your program, first input, then procesing, then output. 

6. Test your program with a wide range of values.



## 7. Input, output and arithmetic expressions 5

1. In VS-Code, open a new Python file. Call it `E7.py`. and add the required header comment block.

2. Using Cartesion coordinates in a plane a point in the plane can be specified by a pair of numbers, $x$ and $y$.  The Euclidean distance between points, $(x_1,y_1)$ and $(x_2,y_2)$ is $ d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$.

3. Write code to have a user enter two points in the plane. 

4. Compute the Euclidean distance between the points and print the result. You will need to do a square root, so you will need the math module. Add the import statement at the top of your program and then you can use ```math.sqrt()``` to compute a square root. 

```Python
import math
``` 

5. Test your program. 



## 8. Functions, main()

1. In VS-Code, open a new Python file. Call it `E8.py`. and add the required header comment block.

2. In this exercise we will create a `main()` function using the code from `E6.py` above.

3. Create a function definition for a `main()` function. As below. 

```python
# 
def main() -> None:
   p_0 = float(input("Enter the initial value of the investment: "))
   print(p_0)
```

4. Run your program. Nothing will happen! A `def` statement defines a function, that is it creates a memory location that it names `main` and puts the indented statements that follow the `def` into that location, but it does not execute the code!

5. Add the last line shown here.

```python
#
def main() -> None:
   p_0 = float(input("Enter the initial value of the investment: "))
   print(p_0)

main()
```

6. Run the program now.

7. Add the code from `E6.py` so that this program behaves exactly as that one does, but using a main function.

8. From now on all programs will be structured like this: 

```Python
# 
# Header comment that includes your name, date, what the program is
# 

# import any modules that you need ... 
import math
import random 

# Any constants that you need ... 

TIP_RATE = 0.10
GST = 0.05 
ASSIGNMENT_WEIGHT = 10

# function definitions ... 

def foo( x:float, n:int)->bool: 
   """ foo takes two parameters and if they are both positive it returns 
   True, else it returns False """
   return x > 0 and n > 0

# A main function. Main usually has no parameters and returns None. 

def main() -> None: 
   """ pass is a placeholder operation that does nothing. It is just there until the readl 
   code gets added"""
   pass 

# invoke main() 

main()
```


## 9. Functions

1. In VS-Code, open a new Python file. Call it `E9.py`. and add the required header comment block.

2. In this exercise we will create a complete program to ask the user for the radius and height of a cylinder and print the volume of that cylinder.

3. To start, create a `main()` function that prompts the user for the values above (radius and height).

3. The volume of a cylinder is given by the formula $V = \pi r^2 h$. The first part, $\pi r^2$ is of course the area of a circle. Create a function called ``area_circle()`` that takes the radius of a circle and returns the area. You can access the value of pi using the math module, ``math.pi``. Remember to add a docstring and type hints. 

4. Test your area function by putting some `print()` statements in your main to print some values of `area_circle()`. A good one is a radius of 1, because the area should be equal to pi. 

5. Once you are convinced your area function is working, delete or comment out the test code.

6. Create a function `volume_cylinder()` that calculates the volume of the cylinder and uses the `area_circle()` function you just created. 

7. Test your program. You should get:

| radius  | height  | volume |
----------|---------|---------|
| 1 | 10| 31.4159 |
| 2 | 10| 125.6637 | 
| 0.5 |1.65 | 1.2959 |



## 10. Decisions

1. In VS-Code, open a new Python file. Call it `E10.py`. and add the required header comment block.

2. In this program we will enter a percentage (grade in a course) and convert it to the following letter grades:

| Percentage | Grade |
|------------|-------|
| 0-49       | Unsatisfactory |
| 50-69      | Satisfactory |
| 70-89       | Good |
| 90-100  | Excellent |

3. Write a main function that prompts to the user to enter the percentage score to 2 decimal places. 

4. Convert that percentage score to an integer using the `math.ceil()` function. This rounds UP. 

5. Write a function, `letter_grade()` that takes the integer percentage as a parameter and returns the appropriate string. This function should use a ``if-elif` structure.  

6. Call `letter_grade()` and print the result. Test your program. 


## 11. Compound Boolean Expressions

1. In VS-Code, open a new Python file. Call it `E11.py`. and add the required header comment block.

2. In this program we will implement the a grocery store discount calculator. In this scenario, a customer will get a 20% discount if they spend more than $100 on the first Tuesday of the month.

3. The basic flow of the program is:

   1. Enter the a amount of the purchase. 

   2. Enter a True/False to indicate if it is the first Tuesday of the month.

   3. If the amount >= 100 and it is the first Tuesday then apply a 20% discount to the total and print a message. Otherwise print a sorry you do not qualify message. 

   4. Calculate the total including the GST and print that out. 

4. Since we are simulating this you can use the following function to determine if it is the first Tuesday. So you only need to input the amount. 

```Python
import random 

PROBABILITY_TUESDAY = 0.4 # the probability that it is the first Tuesday of the month

def first_tuesday()-> bool:
   """ Return True is this is the first Tuesday 
   of the month. Use PROBABILITY_TUESDAY to simulate. 
   """
   n = random.random() # get a number between 0 and 1
   return n < PROBABILITY_TUESDAY

```

5. Test your code with appropriate test values. Try it with 0, below the cut off, at the cut off, above the cut off. The `first_tuesday()` function will randomly give you true or false so test enough times to try all possibilities.



## 12. More decisions

1. In VS-Code, open a new Python file. Call it `E12.py`. and add the required header comment block.

2. Tickets for a show at the Bella Concert Hall are priced as follows:  

| Section | Code | Price |
|---------|------|-------|
| Orchestra | O    | 100  |
| Parterre  | P   | 80 |
| Balcony   | B | 70 |
| Box       | X | 200 |

For the Parterre and Balcony sections seniors (65 years old) get 40% off and children 12 and under get 25% off.

3. Complete and test the following function that calculates the price of a ticket. 

```Python
def ticket_cost(age:int, section:str) -> float:
```

## 13. Even More Decisions

1. In VS-Code, open a new Python file. Call it `E13.py`. and add the required header comment block.

2. In this exercise you will create a function to determine if it good to go outside given some weather information.

3. Prompt the user to enter the temperature, the wind speed, and whether or not there is precipitation.

4. The rules go like this:

   1. If the wind is above 80 kph, do not go out.

   2. If the temperature is less than -25 or more than 37, do not go out.

   3. If there is precipitation and wind above 50 kph, don't do out. 

   4. If there is precipitation and wind above 30 kph and the temperature is less than 0, do not go out.

5. Complete this function which returns True if you should go out, False otherwise.

6. Test your program.

```Python
def outside(temp:int, wind:int, precip:bool) -> bool:
```

> When writing your programs it is good to pay attention to the layout of your code. I like to have two blank lines between sections like imports, constants and before any function definition. I find it easy to read when there is a blank line before the return statment in a function. There should be no lines between the function definition and the docstring, but I like to leave a line after the doctring, before the code starts. 


# 14. While Loops

1. In VS-Code, open a new Python file. Call it `E14.py`. and add the required header comment block.

2. Write a progam that asks the user for a list of words, repeating until a blank word is entered.

3. From the words entered, create a single string that has all of the words separated by commas. Print out that string.

4. Test your code. 

---

> The string method ```.strip()``` will be useful here. It removes any leading or trailing whitespace (spaces, tabs, newlines) from a string. Other string methods can be discovered here: https://www.w3schools.com/python/python_ref_string.asp

---

## 15.  While Loops with a string

1. In VS-Code, open a new Python file. Call it `E15.py`. and add the required header comment block. 

2. Write a function called ``reverse()`` that takes a string as a parameter and returns the string in reverse order. For example, if the function is passed the string "dlroW olleH" it will return the string "Hello World". Your function should use a while loop. 

3. Write a main to test your function thoroughly. 

4. Write a second function called ``reverse_for()`` that does the same thing but uses a for loop rather than a while loop. 


## 16. For Loops

1. In VS-Code, open a new Python file. Call it `E16.py`. and add the required header comment block.

2. In this exercise you will create a function that returns a string consisting of selected letters of the alphabet.

3. Your function should take two parameters: the start letter and the end letter and return a string. 

---

> Python provides some functions for working with characters, converting them to integers and back to characters.

```Python

a_letter = "a"
a_int = ord(a_letter)
print(a_int)

z_int = chr(122)
print(z_int)
```

> Run the code above. You will see that the code for a lower case 'a' is 97 and that the code for a lower case 'z' is 122. 

---

4. Write code to return a string of lower case letters, in order, between the two parameters. For example, if the parameters are 10 and 15 we want to return the 10th to 15th letter of the alphabet, or 'jklmno'.

5. Test your code. For values outside the range use the endpoints. That is if the start letter is 0 or less, use 1. If the end letter is more than 26, use 26.



## 17. More While Loops and a List

1. In VS-Code, open a new Python file. Call it `E17.py`. and add the required header comment block.

2. Convert this for loop to a functionally equivalent while loop: 

```Python
a = []
for q in range(2,10,2):
   a.append( q ** 3)
```


## 18. Looping with Strings 

1. In VS-Code, open a new Python file. Call it `E18.py`. and add the required header comment block.

2. Write a main() function that prompts the user to enter a sentence. 

3. Write a function that converts a sentence to sarcastic text. The first letter should be capitalized and the following letters should alternate between lower and upper case.


## 19. Looping with Strings 

1. In VS-Code, open a new Python file. Call it `E19.py`. and add the required header comment block.

2. Write a main() function that prompts the user to enter a sentence. 

3. Write a function ``nopunct()`` that takes a string as a parameter and returns that string with all punctuation removed. For example, "Help!" would return "Help", "don't" would return "dont", "end." would return "end" and so on. Punctuation includes, '";:.,?!#$%&().

4. Write a function that returns the words in a sentence as a list of individual words. The words should be punctuation free!

5. Test your functions. 


## 20. Star Patterns 

1. In VS-Code, open a new Python file. Call it `E20.py`. and add the required header comment block.
 
2. Write a void function (non-value returning) that prints the following pattern of stars using nested for loops. 
i.e not just print statements! 

```
*
**
***
****
*****
```

3. Add a paramter to your function to set the number of rows printed. i.e. the example is 5. 

4. If that was fun, create functions for each of the following patterns. Write it first with the pattern
given and then add parameters as appropriate to set the size. 

   1. 
   ```
   *****
   ****
   ***
   **
   *
   ```

   2. 
   ```
   *****
   *   *
   *   *
   *   *
   *****
   ```

   3. 
   ```
       *
      ***
     *****
    *******
   *********
   ```

   4. 
   ```
   *
   **
   ***
   ****
   *****
   ****
   ***
   **
   *
   ```

   5. 
   ```
   *       *
    *     *
     *   *
      * * 
       *
      * * 
     *   * 
    *     * 
   *       * 
   ```

   6. 
   ```
       *
      ***
     *****
    *******
   *********
    *******
     *****
      ***
       *
   ```

   7. 
   ```
   **********
    ********
     ******
      ***
       *
   ```


## 21. Files

1. In VS-Code, open a new Python file. Call it `E21.py`. and add the required header comment block.

2. Write a program that prompts for a text file name and a ``word``. 

3. The program will read the text file, line by line and print the lines that contain ``word``. 

4. Add code to make the searching case insensitive. Ensure that leading or trailing blanks are not 
included with ``word``. 


## 22. File and Lists

1. In VS-Code, open a new Python file. Call it `E22.py`. and add the required header comment block.

2. Write a program that prompts for a text file name, reads the contents of the file and stores each 
line as list of words. Words are strings of characters separated by whitespace. 

3. Add code to prompt for a word to find in the file and responds with how many occurences there are 
of that word. The search should not be case sensitive.


## 23. Dot product 

1. In VS-Code, open a new Python file. Call it `E23.py`. and add the required header comment block.

2. Write a function that computes the dot product of two vectors. 
Remember that if you have vectors `x` and `y`, the dot product is $\sum_{i = 0}^{n}{x_i \times y_i}$. 
For this exercise the vector is a list of numbers. 

3. If the vectors are not the same length return 0.

4. Write a `main()` to thoroughly test your function. 


## 24. Files and Lists

1. In VS-Code, open a new Python file. Call it `E24.py`. and add the required header comment block.

2. Write a function that takes a file name as a parameter and returns a list of integers. 
The file should be a text file with a list of integers, one per line. The function should read the 
whole file and add the numbers to the list that it returns. 

3. Test your program with a few different files. 



## 25. Lists 

1. In VS-Code, open a new Python file. Call it `E25.py`. and add the required header comment block.

2. Using your function from E24, write a progam that reads a list of integers from a given file and stores them in a list. 

3. Write this function and test it using the list you read in. 

```Python
def swap(nums: list[int], pos1: int, pos2: int) -> None:
    """ 
    In the list nums swap the value from pos1 with the 
    value from pos2.
    """
```

4. Write a this function and test is using ``swap()`` and the list of numbers you read in. 

```Python
def loop_and_swap (nums: list[int]) -> bool:
    """ Go through the list nums. Compare adjacent 
    values and if they are out of order, call swap 
    to swap them. If a swap occurs, return True, else 
    return False. 
    """
```

5. Write a this function and test is using ``loop_and_swap()`` and the list of numbers you read in. 

```Python
def process(nums: list[int]) -> None:
    """ Call loop_and_swap() until no swaps occur, 
    which means the list is in order. 
    """
    swapped = loop_and_swap(nums)
    while swapped: 
        swapped = loop_and_swap(nums)
    
```

6. Finally, write a main program that reads in a list of numbers, prints that list, calls process with the list, and then prints it again. What is this program doing? How many times does the list get processed? How many times does the program go through the list? 
   

## 26. Input - Various Input functions

1. In VS-Code, open a new Python file. Call it `E26.py`. and add the required header comment block.

2. Write a function ```def enter_list()->list``` which prompts the user to enter a list 
of integers, separated by commas and returns those values as a list of ints. Thoroughly test your function. 

3. Write a function ```def enter_str(prompt:str)->str``` that prompts the user to enter something and if the user enters an empty string, keeps prompting. For example if the function was called like this

```Python
   a = enter_Str("Enter your favourite tree: ")
   print(a)

``` 

A run would look like this if the user entered three blank lines, then the word 'yew'

```
Enter your favoutite tree:
Enter your favoutite tree:
Enter your favoutite tree:    
Enter your favoutite tree: yew
yew
```

4. Write a function ```def yorn()->str``` that prompts the user to enter y or n and returns that value when one of those was entered. This should not be case-sensitive. 

5. Write another function called ``def yes()->bool`` which called yorn and returns True if the user entered 'y' or 'Y' and False otherwise. 

6. Test thoroughly. 


