# Plot some functions to show the differnt growth rates. 
#
# Alan Fedoruk 
# COMP 1701 

import matplotlib.pyplot as plt
import numpy as np

def quad(x:float)->float:
    """A quadratic function. y=x^2+0"""
    return x * x

def exp(x:float)->float: 
    """An exponential function, y=2^x"""
    return 2**x

def linear(x:float)->float:
    """A linear function, y = 2x+0"""
    return 2 * x


# Create x and y Ranges
x = np.linspace(0, 100, 1000)
y1 = quad(x)
y2 = linear(x)
y3 = exp(x)

# Plot the Data
fig, ax = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(8)
ax.plot(x, y1, label='Quadratic f(x)=x**2')
ax.plot(x, y2, label='Linear f(x)=2x')
ax.plot(x, y3, label='Exponential f(x)=2**x')

ax.set_title('Comparing Functions', size=14)
ax.set_xlim(0, 100)
ax.set_ylim(0, 1000)
plt.legend()

# plt.show()
# Rather than show it, save it as a png
plt.savefig("funcs.png")
