#!/bin/bash/env python
import numpy as np

def sequence_a_n(N):
    """This function takes in a finite limit for this sequence and then outputs an array which represents that 
    sequence up to that limit. The book defines n to be a range of even integer from 0 to the defined N """
    n = np.linspace(0,N,N/2+1)
    array = (7.0+1.0/(n+1))/(3.0-(1.0/((n+1)**2)))
    return array
   # print array
    
def test_sequence_a_n():
    """This function tests the sequence defined in the previous function for a value of
    N=100 and compares it to the exact limit when N goes to infinity"""
    exactLimit = 7.0/3
    a_100 = sequence_a_n(100)
    assert (abs(a_100[50] - exactLimit) < 1E-2)

def limit(seq):
    """This funcction takes in a random sequence of numbers and outputs the limit of the
    given sequence if it passes a convergence test. """
    #limitTest1 = abs(seq[n]) - abs(seq[n+1])
    #limitTest2 = abs(seq[n-1]) - abs(seq[n])
    for n in range(len(seq)+1):
        if(abs(seq[n]) - abs(seq[n+1]) < abs(seq[n-1]) - abs(seq[n])):
           return seq[len(seq)-1]
        else:
            return None

def test_limit():
    """We will test the limit function with the sequence b_n = n for n in the interval[0,500]"""
    bn = np.linspace(0,500,501) 
    test =  limit(bn)
    if test == None:
        return False
    else:
        return bn[len(bn)-1]

 
def sequence_D(N):
    """Creates a specified sequence for evaluation. sin(2^(-n))/2^(-n)"""
    n = np.linspace(0,N,N+1)
    Dn = np.sin(2**(-n))/(2**(-n))
    return Dn

def E(f,x,N):
    """This is the second D_n sequence that is defined in the problem that I decided to rename to E """
    n = np.linspace(0,N,N+1)
    h = 2**(-n)
    approx =(f(x+h) - f(x))/h
    return approx

def main():
    """The main function is being used to call the functions defined above and to test their limits."""
    """ an = sequence_a_n(100)
    dn = sequence_D(1000) #sequence defined by sin(2^-n)/2^-n
    e = E(lambda x: np.sin(x), 0,80)
    ePi = E(lambda x: np.sin(x),np.pi,80)
    
    print 'D_n: ', dn
    print 'a_n: ', an
    print 'E: ', e
    print 'E @ x=pi: ', ePi
    print 'Test limit: ', test_limit()
    print 'Limit of a_n: ', limit(an)
    print 'Limit of D_n when n = 1000: ', limit(dn)
    print 'Limit of E at x=0: ', limit(e)
    print 'Limit of E at x = pi: ', limit(ePi)
   
    """
    limit(sequence_a_n(100))

if __name__ == "__main__":
    main()
