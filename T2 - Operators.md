## COMP 1701 

# Tutorial 2 - Operators

This tutorial will involve some work on the computer and some on paper. 
Try solving the following problems by hand in small groups, then check 
your answers using Python's interactive mode. 

### 1. Operators

Python uses the following arithmetic operators. 
This tutorial is intended to get you familiar with how these operators 
work and their precedence (the order in which they are evaluated). 



| Name                  | Operator| Prec.      | Example        | Math Equivalent |
|-----------------------|---------|------------|----------------|----------------|
| Parentheses/brackets	| ()      | 1	       | x = (2 + 3)/2  |  $ x = \frac{2+3}{5}$ |
|			            |         | 	       | x = 2.5 	    |                       |
| Exponentiation        | **      | 2	       | x = 3 ** 2		|  $x = 3^2$            |
| 			            |         | 	       | x = 9			|             |
| Multiplication        | *	      | 3	       | x = 3 * 2.5	|   $ x = 3 \times 2.5$ |
| 	                    | 	      |            | x = 7.5		|  
| Division		        | /	      | 3	       | x = 5 / 2		|  $ x = \frac{5}{2}$ |
|                       |         |            | x = 2.5		|                     |
| Integer Division      | //	  | 3	       | x = 5 // 2     |  N/A - round down after dividing |
| 	                    |         |            | x = 2		    |  
| Modulo                | %	      | 3	       | x = 5 % 2      |  N/A - remainder after dividing |
|                       |         |            | x = 1          |  |
| Addition	            | +	      | 4          | x = 2 + 2		|  $ x = 2 + 2$ |
|                       |         |            | x = 4			|  |
| Subtraction	        | -	      | 4	       | x = 5 - 6		|  $x = 5-6$ |
| 	                    |         |            | x = -1			|  |

Python follows the same precedence as standard math (BEDMAS). 
When two operators of the same precedence are on the same line, the operation happens from left to right. 

> At all times if adding brackets will clarify how the expression should be evaluated, add the brackets! 

### 2. Order of operations

The concept of an **expression** and the process of **evaluating** expressions is fundamental in programming. An arithmetic expression consists of *atoms* and *opperators*. 
Atoms can be *literals* like 5 or 2.1 or *variables* that we will look at below. 

On paper or a whiteboard, evaluate the following arithmetic expressions.

1. `2 * (20 /4 + 1) + 5`
2. `4 * 3 / 6`
3. `4 / 6 * 3`
4. `3 * 4 / 6`

Next, try the following to test out the new operators // and \%

1. `4 // 6 * 3`
2. `3 * 4 // 6`
3. `7 % 3`
4. `4 + 7 % 3 - 5`
5. `(4 + 7) % 3 - 5`

On a computer (one per group), open a Python interpreter. Enter the expressions above to Check your results. Were your calculations correct?

### 3. Working with Variables

Given the following variable definitions

```Python
x = 2.5
y = -1.5
m = 18
n = 4
```

What are the values of the following expressions? Again, evaluate first by hand, then check your work using a Python interpreter. 

 1. ``x + n * y - (x + n) * y``
 2. ``m // n + m % n``
 3. ``5 * x - n // 5``
 4. ``1 - (1 - (1 - (1 - (1 - n))))``


### 4. Translating math to code

By hand, write Python arithmetic expressions for each of the following. Assume the variables have already been declared and assigned. 
Since you are writing a math formula, it is okay for your variable names to be short (e.g. just "A").


1. $A + \frac{B}{C+D} $
2. $(X-1)(Y-4)$ 
3. $\frac{-B + X}{2A}$ 
4. $XY^2Z$ 

How would you check if your expressions are correct?

### 5. Algorithm design

You are coding an online interface to a board game called [Incan Gold](https://www.eaglegames.net/Incan-Gold-2018-p/102197.htm) where players explore a temple and try to collect as many gems as they can. Gems are split equally between each player, with any amount leftover added to a separate pile.

Given the total number of gems and number of players, write an algorithm to calculate how many gems are received by each player and how many are leftover. The result should be displayed to the user.

Write out the steps of the algorithm in pseudocode, as a flowchart, or in point form, whatever makes the most sense to you.

> Hint: Before starting to design the algorithm, check your understanding by working through a couple of examples, such as 11 gems and 4 players, or 13 gems and 5 players.


### 6. Code tracing

For each of the following code snippets, predict what will be written to the screen. You may find it helpful to write down the intermediate values of each variable when they are reassigned.

1. 
```Python
freeze = 32
boil = 212
freeze = 0
boil = 100
print(freeze)
print(boil)
```
2. 
```Python
doughnuts = 6
friends = 3
print("We all get", doughnuts/(friends + 1), "doughnuts.")
```
3. 
```Python
doughnuts = 6
friends = 3
total_peeps = friends + 1
whole_doughnuts = doughnuts // total_peeps
leftover = doughnuts % total_peeps
print("We all get", whole_doughnuts, "whole doughnuts!")
print("There are", leftover, "doughnuts left over.")
```
4. 
```Python
beta = 9
alpha = 3 * beta
print(alpha, ",", beta)
alpha = alpha + 1
print("alpha,beta")
beta = beta + beta
print(alpha, ",", beta)
```