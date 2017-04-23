"""

Filename: extended_euclidean.py
Author: Steven
Date Last Modified: 3/12/2017
Email: bouwkast@mail.gvsu.edu

"""



def xgcd(a,b):
    # These first two lines are similar to the setup of the matrix multiplication method
    x_prev, x = 1, 0  # same as x_prev = 1 and x = 0
    y_prev, y = 0, 1  # same as y_prev = 0 and y = 1
    while b:  # stop when we hit 0
        quotient = a//b  # specify that we want integer division
        x, x_prev = x_prev - quotient*x, x
        y, y_prev = y_prev - quotient*y, y
        a, b = b, a % b  # a = b and b = a%b
    return a, x_prev, y_prev  # tuple containing the gcd, and solutions for x and y

print(xgcd(3, 32770))
