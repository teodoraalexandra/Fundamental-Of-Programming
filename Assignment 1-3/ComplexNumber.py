'''
Assignment 2 - Complex Number Menu
'''

'''
Each complex number has an unique real part (integer) and an unique
imaginary part (integer).
The application will have a menu-driven user interface and will provide
the following features:

1. Add a complex number
2. Print the entire list of complex numbers
3. Print only the numbers which are real (has the imaginary part 0)
   *This is the sequence number 5 from assignment
4. Print the numbers with a strictly increasing real part
   *This is the sequence number 1 from assignment
5. Exit
'''

def createNumber(realPart, imaginaryPart):
    return (realPart, imaginaryPart)

def getReal(number):
    return number[0]

def getImaginary(number):
    return number[1]

def toString(number):
    '''
    Building the string representation for the number
    Input: the complex number
    Output: the string
    '''
    if int(getImaginary(number)) == 0:
        return "z = " + str(getReal(number))
    elif int(getReal(number)) == 0:
        return "z = " + str(getImaginary(number)) + "i"
    elif int(getImaginary(number)) < 0:
        return "z = " + str(getReal(number)) + " " + str(getImaginary(number)) + "i"
    else:
        return "z = " + str(getReal(number)) + " + " + str(getImaginary(number)) + "i"

'''
User interface functions
'''

def __printMenu():
    menuString = '\nMenu:\n'
    menuString += '\t 1 - Add complex number\n'
    menuString += '\t 2 - Print all complex numbers\n'
    menuString += '\t 3 - Print all complex numbers which are real\n'
    menuString += '\t 4 - Print all complex numbers with a strictly increasing real part\n'
    menuString += '\t 5 - Exit\n'
    print(menuString)

def start():
    numberList = []
    testInit(numberList)

    stop = False
    while stop == False:
        __printMenu()
        command = input('Enter command: ')
        if command == '1':
            __addSubmenu(numberList)
        elif command == '2':
            __printSubmenu(numberList)
        elif command == '3':
            __printReal(numberList)
        elif command == '4':
            __printIncreasing(numberList)
        elif command == '5':
            stop = True
        else:
            print('This is not a valid command! Try again.')

def __addSubmenu(numberList):
    '''
    Adding a complex number
    '''
    realPart = input('Enter the real part: ')
    imaginaryPart = input('Enter the imaginary part: ')

    number = createNumber(realPart, imaginaryPart)
    numberList.append(number)

def __printSubmenu(numberList):
    '''
    Printing all complex numbers from the list
    '''
    for number in numberList:
        print(toString(number))

def __printReal(numberList):
    '''
    Printing all complex numbers from the list which has imaginary part 0
    '''
    for number in numberList:
        if int(getImaginary(number)) == 0:
            print(toString(number))

def __printIncreasing(numberList):
    '''
    Printing all complex numbers with a strictly increasing real part
    '''
    for number in numberList:
        if int(getReal(number)) > int(getImaginary(number)):
            print(toString(number))

'''
Here are the tests
'''

def testInit(numberList):
    numberList.append(createNumber(-7, 8))
    numberList.append(createNumber(4, -6))
    numberList.append(createNumber(2, 3))
    numberList.append(createNumber(0, 0))
    numberList.append(createNumber(-4, -5))
    numberList.append(createNumber(2, 0))
    numberList.append(createNumber(0, -3))
    numberList.append(createNumber(6, 5))
    numberList.append(createNumber(8, 0))
    numberList.append(createNumber(0, 5))

def testAddNumber():
    pass

def testPrintNumber():
    pass

def runAllTests():
    numberList = []
    testInit(numberList)
    testAddNumber(numberList)
    testPrintNumber(numberList)

start()

