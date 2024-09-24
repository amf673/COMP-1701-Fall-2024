## COMP 1701 

# Lab 2 - Input-Processing-Output

The goals of this lab are:

1. Use the ``print()`` and ``input()`` functions
2. Cast string input to ``float`` or ``int``
3. Perform some arithmetic calculations
4. Use the math module

## The Exponentional Function

An exponential function is one of the form $y = m^x$. $m$ is a constant and $x$ is a variable. Something that is growing at a steady rate is growing exponentially (even if the rate is small). Many things in the world can be modeled with an exponential function (compound interest, population growth). It is important to understand what exponential growth means, so important that the late physicist [Albert Allen Bartlett](https://en.m.wikipedia.org/wiki/Albert_Allen_Bartlett) said,  

> The greatest shortcoming of the human race is our inability to understand the exponential function.

He has a great [video](https://m.youtube.com/watch?v=kZA9Hnp3aV4) explaining what he means.

In this lab we will exercise our skills with Python ``input()``, ``output()``, casting string values to ``float``s and ``int``s using ``float()`` and ``int()`` and writing arithmetic expressions using examples of exponential functions. We will introduce the math module which provides a many useful mathematical functions.

For the following exercises, create a Python script called ``L2.py``.  Add an an appropriate header comment and then add the code to solve the problems, one after the other. Before each section add a comment stating which problem you are solving.

## Exercises

### 1. Compound Interest

One of the common uses of the exponential function is calculating the value of an investment that is growing with compound interest (compounding means that interest is added to the investment and the next interest calcuation is on that new higher amount). In simple interest you calculate the interest from the original amount.

If you invest $100 at a rate of 12 percent (0.12) for 4 years, you will have a formula of

$PS(n) = P_0 + (P_0 \times r \times t)$

Where $PS(n)$ is the value of the an investment of $P_0$ after $t$ years at interest rate $r$.

$PS(4) = 100 + 100 \times 0.12 \times 4  = 148.00$

If the interest is compounding we calculate the years interest on the new amount, thus

$P(1) = 100 + (100*0.12) = 112$

$P(2) = 112 + (112*0.12) = 125.44$

$P(3) = 125.44 + (125.44*0.12) = 140.4928$

$ P(4) = 140.4928 + (140.4928*0.12) = 157.351936$

Thankfully there is a simple formula to calculate this

$P(t) = P_0 (1 + r) ^t$

$P(t)$ is the value of an investment of $P_0$ after $t$ years at a compound interest rate of $r$. And we can see that

$P(4) = 100 (1 + 0.12) ^ 4 = 100( 1.12) ^ 4 = 100(1.57351936) = 157.351936$

So you want compond interest for your investments.

#### Write code to implement this pseudo code

```None
1. Ask the user for the initial value of the investment, p_0
2. Ask the user for the interest rate (as a decimal, i.e. 0.05 for 5%), r
3. Ask the user for the number of years to invest, t
4. Calculate the value of the investment using the formula above. (p = p_0(1+r)**t)
5. Print the result
```

Notes:

1. All input values are floating point numbers. ``input()`` returns a ``str``, so you will need to cast that to a ``float``.
2. The output should look exactly like the sample below. Note how the interest rate and the final value are displayed. Python has a built in function ``round(a, n)`` that will return its argument ``a`` rounded to ``n`` digits. `round()` will be handy.
3. Assume that only valid values are entered by the user. 

A Sample Run:

```None
Enter the initial value of the investment: 100
Enter the interest rate: 0.12
Enter the number of years to invest: 4
An investment of 100.0 at 12.0 % will be worth 157.35 after 4.0 years.
```

Check your program with a variety of values. Try rates of 0, negative, or 1.0, at least.

### 2.  Doubling

A special case of the interest formula occurs when ``r`` is 1, or 100%. The quantity doubles in every time step or event. In that case we get

$P(t) = P_0(1+1)^t = P_0(2)^t$

A real world example of this is [Moore's Law](https://en.wikipedia.org/wiki/Moore's_law) which says that the number of transisters that can be packed onto an integrated circuit doubles about every two years. This phenomena has driven the computer industry since the 1960s. Essentially every couple of years, for about the same money, you can get a computer that is twice as powerful. Things have slowed a bit of late.

Another example is paper folding. It is easy to see that every time you fold a paper in half, the resulting stack will double in thickness. As you have probably found out by trying, you can only fold a paper so many times before it gets difficult and then imposible to do another fold. This is somewhere around 7 in most cases. There is a theoretical limit of 12:

> In late 2001 and early 2002, Britney Gallivan proved the minimum length of paper necessary to fold it in half a certain number of times and folded a 4,000-foot-long (1,200 m) piece of toilet paper twelve times https://en.wikipedia.org/wiki/Mathematics_of_paper_folding#Britney_Gallivan

But we are going to do this as more of a thought experiment and we will assume you can just keep folding. We want to know how thick the folded paper will be if we could fold it 2, 5, 10, 50 or 100 times. Write code to do the following:

```None
1. Set the thickness of the paper, thickness, to 0.05mm (a typical sheet of paper)
2. Ask the user to enter the number of folds to make, f
3. Calculate the thickness of the folded stack with the doubling formula 
4. Print the result in meters
```

A sample run is

```None
Enter the number of folds (>0): 5
A paper 5e-05 m thick if folded 5 times, would be 0.0016 m thick.
```

Try your program for a number of values, 0, 1, 5, 10, 20, 50, 100

How thick is the pile with 100 folds? To help understand the thickness note 1 km = 1000 m that 1 light year = $9.46 \times 10^{15}$ m and that the diamter of the [observable universe](https://en.wikipedia.org/wiki/Observable_universe) is $8.8 \times 10^{26} m$.

The power of doubling is awesome.

### 3. Doubling Times

It is often useful to be able to calculate the doubling time of some value that is growing exponentially. For example, Calgary has an annual population growth rate of about 3%. How long before the city doubles in population?

The formula for doubling time is

$T_d = \frac{ln(2)}{ln(1+\frac{r}{100})}$

and this is approximately equal to

$T_{approx} = \frac{70}{R}$

where $r$ is the growth rate in percent. The approximation works well for growth rates < 15%.

Write a program to prompt the user for the growth rate and print out the approximate doubling time.

Add to your program so that it also calculates the exact doubling time. For this one we will need a function to calculate the ***natural logarithm***, ``ln(x)``. The math module has such a function. To use it add this line to the top of your program (after the comment block and before any other code).

```Python
import math
```

You can then use ``math.log(x)`` (I am not sure why it is not called ``ln(x)``) to obtain the value for the natural (base e) logarithm of x.

Output should look like this:

```None
Enter the growth rate in percent: 5
At a growth rate of 5.0 doubling is approximately 14.0 and exactly 14.21
The difference is  0.2066990828904629
```

### 4. Submission

Ensure that your program

- Runs.
- Has an appropriate header comment block.
- Has comments indicating where your solution to each question starts.
- Uses appropriate variable names, both syntactically correct and adhering to the conventions given in class.
- Your output is as close to the samples given as you can make it.

Save your file, ``L2.py`` and submit to the dropbox provided on D2L.

### Growth Rates

This plot:
![center](funcs.png)

show the difference between a linear, quadratic and exponential growth. This graph was created with ``mathplotlib``, one of the many wonderful packages that are available for Python. The code is posted with this tutorial, ``plot.py`` if you are interested.
