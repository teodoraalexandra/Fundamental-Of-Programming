'''
Created on Oct 19, 2016

@author: Arthur

This is the functions module of the application. It contains those functions that actually implement the required features.

!NB
    The current module MUST NOT contain any I/O, it must communicate with other modules exclusively using function parameters, returns and exceptions
'''
from seminar04.domain.complex import isReal, modulus, getImag, getReal, create, equal

def addNumber(numberList, number):
    """
    Add complex number to list
    Input: numberList - The list to add to 
           number - The number to add
    Output: -
    Exceptions: -
    """
    numberList.append(number)
    
def removeNumberAtPos(numberList, pos):
    """
    Remove complex number from list given its position
    Input: numberList - The list 
         pos - The position from which number is removed
    Output: -
    Exceptions: ValueError if position invalid!
    """
    if pos < 0 or pos >= len(numberList):
        raise ValueError("Invalid position!")
    numberList.pop(pos)

def removeNumber(numberList, number):
    """
    Remove all appearances of the complex number from list
    Input: numberList - The list 
           number - The number to remove
    Output: The filtered list
    Exceptions: -
    """
    while number in numberList :
        numberList.remove(number)

def filterByReal(numberList):
    """
    Filter all real numbers
    Input: A list of complex numbers to filter
    Output: The list of real numbers from input list
    Exceptions: -
    """
    res = []
    for number in numberList:
        if isReal(number):
            res.append(number)
    return res

def filterByModulus(numberList, value):
    """
    Filter all numbers with modulus>value
    Input: numberList - a list of complex numbers
           value - modulus value to filter
    Output: The list of filtered numbers
    Exceptions: -
    """
    res = []
    for number in numberList:
        if modulus(number) >= value:
            res.append(number)
    return res

def complexToStr(number):
    """
    Convert complex number to string
    Input: The complex number
    Output Its string representation
    Exceptions: -
    """
    result = ""
    if getReal(number) == 0 and getImag(number) == 0: 
        return "0"
    if getReal(number) != 0:
        result += str(getReal(number))
    if getReal(number) != 0 and getImag(number) > 0:
        result += "+"
    if getImag(number) != 0:
        if getImag(number) == 1:
            result += "i"
        elif getImag(number) == -1:
            result += "-i"
        else:
            result += str(getImag(number)) + "i"
    return result

def listToStr(numberList):
    """
    Convert list of numbers to string
    Input: A list of complex numbers
    Output: The string representation
    Exceptions: -
    """
    if len(numberList) == 0:
        return "list is empty"
    string = ""
    for z in numberList:
        string += complexToStr(z)
        string += " "
    return string 

def testComplexToStr():
    assert complexToStr(create(0, 0)) == "0"
    assert complexToStr(create(1, 0)) == "1"
    assert complexToStr(create(-1, 0)) == "-1"
    assert complexToStr(create(1, 1)) == "1+i"
    assert complexToStr(create(1, -1)) == "1-i"
    assert complexToStr(create(2, 2)) == "2+2i"
    assert complexToStr(create(-1, -3)) == "-1-3i"
    assert complexToStr(create(-10, -99)) == "-10-99i"

def testAddNumber():
    l = []
    addNumber(l, create(1, 2))
    assert len(l) == 1 and getReal(l[0]) == 1 and getImag(l[0]) == 2
    addNumber(l, create(3, 4))
    assert len(l) == 2 and getReal(l[1]) == 3 and getImag(l[1]) == 4
    
def testRemoveNumber():
    l = [create(0, 0), create(1, 2), create(1, 2), create(1, 2), create(3, 4), create(5, 6)]
    removeNumberAtPos(l, 0)
    removeNumberAtPos(l, 4)
    assert len(l) == 4
    assert getReal(l[0]) == 1 and getImag(l[0]) == 2
    assert getReal(l[3]) == 3 and getImag(l[3]) == 4
    removeNumber(l, create(1, 2))
    assert len(l) == 1
    removeNumber(l, create(3, 4))
    assert len(l) == 0

def testFilterByReal():
    l = [create(0, 0), create(1, 2), create(1, 2), create(1, 2), create(3, 4), create(5, 6)]
    res = filterByReal(l)
    assert len(res) == 1 and equal(res[0],create(0,0))