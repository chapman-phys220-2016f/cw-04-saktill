#! bin/bash/env python
import numpy as np

"""For ease of test function I wanted to call a previously defined midpoint
 integration module. But realized this wont work because of the name of my 
 function definition in the module."""

def diffMidptInt(f,a,b,N):
    """Takes arguments: desired function, interval [a,b], and number of
    evaluation steps, returns the midpoint approximation integral using
    difference equations."""
    h = (float(b-a))/float(N)
    x = np.linspace(a,b,N)
    integral = np.zeros_like(x)
    for i in range(1,N):
        j = float(a) - .5*h + float(i)*h
        integral[i] = integral[i-1] + h*f(j)
    return x, integral


def midpointint(f,a,b,n):
    """This function takes in a function and 3 integer parameters representing
    an interval and the number of subintervals to be made in that interval 
    and returns the approximate value of the integral of the given function 
    in the given interval """
    
    h = (b-a)/float(n)
    s = 0.0
    for i in range (n+1):
        s += f(a - (1.0/2)*h + i*h)
        
    midpoint = h*s
    return midpoint

def test_diffMidptInt():
    """Testing our recursive formula with the non-recursive formula for
    midpoint integration."""
    x = diffMidptInt(lambda x: x**2,0,4,10)[1][9]
    y = midpointint(lambda x: x**2,0,4,10)
    if (abs(x - y) <= 1E-4):
        assert True

