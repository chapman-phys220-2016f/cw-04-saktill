#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt 

#Exercise A.2

"""This program includes five functions, each defined as a different sequence
to estimate pi, up to n steps."""



def getN(n):
	"""Just makes an array from 1 to n. Mainly here to be called in seq1."""
	array = np.arange(1,n+1)
	return array

def f1(n):
	"""returns the a_n element of the sequence."""
	An = 0
	#sum over k from 1 to n
	for k in range(1, int(n)+1):
		k = float(k)
		An += ((-1.0)**(k+1.0))/(2*k-1.0)
	An *= 4.0
	return An

def seq1(n, f):
	"""Calls the function of the sequence, returning an array of the elements
	of the sequence from a_1 to a_n, taking args n, f, where n is an int and
	f is a vectorizable function; provided functions are f1, f2, f3, f4, f5.
	"""

	#vectorize the formula for the sequence
	vf = np.vectorize(f)
	
	#create an array of integers from 1 to n, defines final array as the 
	#function acting on that
	array = vf(getN(n))
	return array

def f2(n):
	"""Returns the b_n element of the sequence."""
	Bn = 0
	#sum over k from 1 to n
	for k in range(1, int(n)+1):
		k = float(k)
		Bn += 1/k**2.0
	Bn *= 6.0
	Bn **= 0.5
	return Bn 

def f3(n):
	"""Returns the c_n element of the sequence."""
	Cn = 0
	for k in range(1, int(n)+1):
		k = float(k)
		Cn += k**(-4.0)
	Cn *= 90.0
	Cn **= .25
	return Cn

def f4(n):
	"""Returns the d_n element of the sequence."""
	Dn = 0
	for k in range(0, int(n)+1):
		k = float(k)
		Dn += ((-1.0)**k)/((3.0**k)*(2.0*k+1.0))
	Dn *= (6.0/np.sqrt(3.0))
	return Dn

def f5(n):
	En = 0
	for k in range(0, int(n)+1):
		k = float(k)
		En += (4.0*((-1.0)**k))/((5.0**(2.0*k+1.0))*(2.0*k+1.0)) 
		En -= ((-1.0)**k)/((239.0**(2.0*k+1.0))*(2.0*k+1.0))
	En *= 4.0
	return En

def plotSeq(n,f):
	"""Plots the sequence, a_n vs n, taking a defined function f1, f2, 
	f3, f4 or f5 as a function to plot. (Does this by calling seq1, and 
	plotting the result of that against getN()."""
	plt.plot(getN(n), seq1(n,f), 'bo')
	plt.xlabel('n')
	plt.ylabel('a_n')
	plt.show()

def plotAll(n):
	"""Plots all the sequences, to show how quickly they converge to pi."""
	plt.hold('on')
	plt.plot(getN(n),seq1(n,f1),getN(n),seq1(n,f2),getN(n),seq1(n,f3),getN(n),seq1(n,f4),getN(n),seq1(n,f5),)
	plt.legend(['Seq1','Seq2','Seq3','Seq4','Seq5'])
	plt.show()


#Following tests test the designated functions,
#for n = 1
def test_f1():
	shouldBe = 4.0
	assert shouldBe == f1(1)

def test_f2():
	shouldBe = 6.0**.5
	assert shouldBe == f2(1)

def test_f3():
	shouldBe = 90.0**.25
	assert shouldBe == f3(1)

def test_4():
	shouldBe = -((6.0)/(np.sqrt(3.0)))*(1.0/9.0)
	assert shouldBe == f4(1)

def test_5():
	shouldBe = -(16.0)/(375.0) + 4.0/((239.0**3.0)*3.0)
	assert shouldBe == f5(1)




def test_seq1():
	testResult = np.array([4.0])
	assert testResult == seq1(1, f1)
