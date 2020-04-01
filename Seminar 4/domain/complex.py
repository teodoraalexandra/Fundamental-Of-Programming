'''
Created on Oct 19, 2016

@author: Arthur

This module contains the operations required for our complex number data type

!NB 
    Data Type = domain + operations
    The current module MUST NOT contain any I/O, it must communicate with other modules exclusively using function parameters, returns and exceptions
'''
from math import sqrt

def create(real, imag=0):
    return [real, imag]

def getReal(z):
    return z[0]

def getImag(z):
    return z[1]

def equal(c1, c2):
    """
    Test if two complex number are equal
    Input: Two complex numbers
    Output: True if numbers are equal, false otherwise
    Exceptions: -
    """
    return getReal(c1) == getReal(c2) and getImag(c1) == getImag(c2)

def isReal(number):
    """
    Test if given number is real
    Input: A complex number
    Output: True if number is real, False otherwise
    Exceptions: -
    """
    return getImag(number) == 0

def modulus(number):
    """
    Calculates the modulus of a complex number
    Input: A complex number
    Output: The value of the modulus
    Exceptions: -
    """
    return sqrt(getReal(number) ** 2 + getImag(number) ** 2)

def sum(c1, c2):
    """
    Calculates the sum of two complex numbers
    Input: A pair of complex numbers
    Output: Sum of given numbers
    Exceptions: -
    """
    return create(getReal(c1) + getReal(c2), getImag(c1) + getImag(c2))

def testEqual():
    assert equal(create(0, 0), create(0, 0)) == True
    assert equal(create(1, -2), create(1, -2)) == True
    assert equal(create(1, 0), create(0, 1)) == False
    assert equal(create(0, -1), create(-1, 0)) == False

def testIsReal():
    assert isReal(create(0, 0)) == True
    assert isReal(create(1, 0)) == True
    assert isReal(create(-1, 0)) == True
    assert isReal(create(0, 1)) == False
    assert isReal(create(0, -1)) == False
    assert isReal(create(-1, -1)) == False

def testModulus():
    assert modulus(create(0, 0)) == 0
    assert modulus(create(1, 0)) == 1
    assert modulus(create(0, -1)) == 1
    assert modulus(create(3, 4)) == 5

def testSum():
    assert equal(sum(create(0, 0), create(0, 0)), create(0, 0))
    assert equal(sum(create(1, 0), create(0, 1)) , create(1, 1))
    assert equal(sum(create(-1, 2), create(1, -2)) , create(0, 0))
    assert equal(sum(create(2, 2), create(3, 4)) , create(5, 6))
