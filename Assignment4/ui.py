from functions import *
from copy import deepcopy
from domain import *

import datetime
now = datetime.datetime.now()

#Printing menu

def printMenu():
    print('\n')
    print('Expenses application menu: ')
    print('   add for adding a new expense to current day')
    print('   insert for adding a new expense')
    print('   remove for removing a given expense')
    print('   list for listing expenses with a given property')
    print('   sum for computing the total expense for a category')
    print('   max day for showing the day with the biggest expense')
    print('   sort for sorting certain expenses')
    print('   filter for filtering expenses with a given property')
    print('   undo for reversing the last command executed')
    print('   end for closing the application')


#User interface functions with validation

#ADD USER INTERFACE FUNCTION
def add_ui(listOfExpenses, m, undoList):
    '''
    Read the sum and the type and add to the list of expenses to current day
    add <sum> <category>
    '''
    recordForUndo(listOfExpenses, undoList)
    a = now.day

    if len(m) != 3:
        raise SyntaxError('You must add only sum and category!')

    b = m[1]
    if b.isnumeric() is False:
        raise SyntaxError('The sum must be numeric!')
    else:
        b = int(m[1])
        if b < 0:
            raise ValueError('The sum must be positive!')

    c = m[2]
    if c != "housekeeping" and c != "food" and c != "transport" and c != "clothing" and c != "internet" and c != "others":
        raise ValueError('This category does not exist!')

    expense = createExpense(a, b, c)
    addExpense(expense, listOfExpenses)

#INSERT USER INTERFACE FUNCTION
def insert_ui(listOfExpenses, m, undoList):
    '''
    Read the day, the sum and the type and insert to the list of expenses
    insert <day> <sum> <category>
    '''
    recordForUndo(listOfExpenses, undoList)

    if len(m) != 4:
        raise SyntaxError('You must add day, sum and category!')

    a = m[1]
    if a.isnumeric() is False:
        raise SyntaxError('The day must be numeric!')
    else:
        a = int(m[1])
        if a < 1 or a > 31:
            raise ValueError('Invalid day! Give a day between 1 and 31')

    b = m[2]
    if b.isnumeric() is False:
        raise SyntaxError('The sum must be numeric!')
    else:
        b = int(m[2])
        if b < 1:
            raise ValueError('The sum must be greater than 1!')

    c = m[3]
    if c!= "housekeeping" and c!= "food" and c!= "transport" and c!= "clothing" and c!= "internet" and c!="others":
        raise ValueError('This category does not exist!')

    expense = createExpense(a, b, c)
    addExpense(expense, listOfExpenses)

#REMOVE USER INTERFACE FUNCTION
def remove_ui(listOfExpenses, m, undoList):
    '''
    Remove the expenses which have a given property
    remove <day>
    remove <start day> to <end day>
    remove <category>
    '''
    recordForUndo(listOfExpenses, undoList)

    if len(m) == 1 or len(m) == 3 or len(m) >= 5:
        raise SyntaxError('Invalid command!')

    a = m[1]
    if a.isnumeric() is True:
        a = int(m[1])
        if a < 1 or a > 31:
            raise ValueError('Invalid day! Give a day between 1 and 31')
        if len(m) == 4:
            if str(m[2]) == 'to':
                b = m[3]
                if b.isnumeric() is False:
                    raise ValueError("The end day must be an integer!")
                else:
                    b = int(m[3])
                    if b < 1 or b > 31:
                        raise ValueError('Invalid day! Give a day between 1 and 31')
                    removeStartToEnd(listOfExpenses, a, b)
            else:
                raise SyntaxError('Invalid command!')

        elif len(m) == 2:
            removeDay(listOfExpenses, a)

    else:
        if len(m) != 2:
            raise SyntaxError('Invalid command!')
        if m[1] != "housekeeping" and m[1]!= "food" and m[1]!= "transport" and m[1]!= "clothing" and m[1]!= "internet" and m[1]!="others":
            raise ValueError('This category does not exist!')
        removeCategory(listOfExpenses, a)

#LIST USER INTERFACE FUNCTION
def list_ui(listOfExpenses, m):
    '''
    List the list of expenses which have a given property
    list
    list <category>
    list <category> [ < | = | > ] <value>
    '''
    if len(m) == 1:
        string(listAll(listOfExpenses))

    elif len(m) == 2:
        if m[1] != "housekeeping" and m[1]!= "food" and m[1]!= "transport" and m[1]!= "clothing" and m[1]!= "internet" and m[1]!="others":
            raise ValueError('This category does not exist!')
        a = m[1]
        string(listCategory(listOfExpenses, a))

    elif len(m) == 4:
        if m[1] != "housekeeping" and m[1]!= "food" and m[1]!= "transport" and m[1]!= "clothing" and m[1]!= "internet" and m[1]!="others":
            raise ValueError('This category does not exist!')

        a = m[1]
        b = m[3]
        if b.isnumeric() is False:
            raise ValueError('You must introduce a numeric value for comparation')

        b = int(m[3])
        if m[2] == ">":
            string(listGreater(listOfExpenses, a, b))

        elif m[2] == "=":
            string(listEqual(listOfExpenses, a, b))

        elif m[2] == "<":
            string(listSmaller(listOfExpenses, a, b))

        else:
            raise SyntaxError('Invalid command. You are allow to enter <,> or =')

    else:
        raise SyntaxError('Invalid syntax!')


def sum_ui(listOfExpenses, m):
    '''
    Write the total expense for a category
    sum <category>
    '''
    if len(m) != 2:
        raise SyntaxError('Invalid syntax!')
    if m[1] != "housekeeping" and m[1] != "food" and m[1] != "transport" and m[1] != "clothing" and m[1] != "internet" and m[1] != "others":
        raise ValueError('This category does not exist!')
    a = m[1]
    print('Total sum of expenses for category', a,'is',sum(listOfExpenses, a))

def max_ui(listOfExpenses, m):
    '''
    Write the day with the maximum expenses
    max day
    '''
    if len(m) != 2:
        raise SyntaxError('Invalid syntax')
    if m[1] != 'day':
        raise SyntaxError('Invalid syntax')
    print('The day with maximum expenses is:',max(listOfExpenses))

def sort_ui(listOfExpenses, m):
    '''
    Sort the expenses in ascending order by amount of money spent
    sort <day>
    sort <category>
    '''
    if len(m) != 2:
        raise SyntaxError('Invalid Syntax')
    a = m[1]
    if a.isnumeric() is False:
        if m[1] != "housekeeping" and m[1] != "food" and m[1] != "transport" and m[1] != "clothing" and m[1] != "internet" and m[1] != "others":
            raise ValueError('This category does not exist!')
        print(string(sortCategory(listOfExpenses, a)))
    else:
        a = int(m[1])
        if a < 1 or a > 31:
            raise ValueError('Invalid day! Give a day between 1 and 31')
        print(string(sortDay(listOfExpenses, a)))

def filter_ui(listOfExpenses, m, undoList):
    '''
    Filter the list of expenses which have a given property
    filter <category>
    filter <category> [ < | = | > ] <value>
    '''
    recordForUndo(listOfExpenses, undoList)

    if len(m) == 2:
        if m[1] != "housekeeping" and m[1]!= "food" and m[1]!= "transport" and m[1]!= "clothing" and m[1]!= "internet" and m[1]!="others":
            raise ValueError('This category does not exist!')
        a = m[1]
        print(string(filterCategory(listOfExpenses, a)))

    elif len(m) == 4:
        if m[1] != "housekeeping" and m[1]!= "food" and m[1]!= "transport" and m[1]!= "clothing" and m[1]!= "internet" and m[1]!="others":
            raise ValueError('This category does not exist!')

        a = m[1]
        b = m[3]
        if b.isnumeric() is False:
            raise ValueError('You must introduce a numeric value for comparation')

        b = int(m[3])
        if m[2] == ">":
            print(string(filterGreater(listOfExpenses, a, b)))

        elif m[2] == "=":
            print(string(filterEqual(listOfExpenses, a, b)))

        elif m[2] == "<":
            print(string(filterSmaller(listOfExpenses, a, b)))

        else:
            raise SyntaxError('Invalid command. You are allow to enter <,> or =')

    else:
        raise SyntaxError('Invalid syntax!')

#UNDO FUNCTIONS

def recordForUndo(listOfExpenses, undoList):
    undoList.append(deepcopy(listOfExpenses))

def undo_ui(listOfExpenses, undoList, initialList):
    if undoList == initialList:
        print('No more undos!')
    listOfExpenses[:] = []
    listOfExpenses.extend(deepcopy(undoList.pop()))


def run():
    '''
        Implement user interface
    '''
    listOfExpenses = []
    testInit(listOfExpenses)
    undoList = deepcopy(listOfExpenses)
    initialList = deepcopy(listOfExpenses)
    commands = {'add': add_ui, 'insert': insert_ui, 'remove': remove_ui, 'list': list_ui, 'sum': sum_ui, 'max': max_ui, 'sort': sort_ui, 'filter': filter_ui, 'undo': undo_ui}

    while True:
        printMenu()
        m = input().split(" ")

        try:
            if m[0] == 'add':
                add_ui(listOfExpenses, m, undoList)
            elif m[0] == 'insert':
                insert_ui(listOfExpenses, m, undoList)
            elif m[0] == 'remove':
                remove_ui(listOfExpenses, m, undoList)
            elif m[0] == 'list':
                list_ui(listOfExpenses, m)
            elif m[0] == 'sum':
                sum_ui(listOfExpenses, m)
            elif m[0] == 'max':
                max_ui(listOfExpenses, m)
            elif m[0] == 'sort':
                sort_ui(listOfExpenses, m)
            elif m[0] == 'filter':
                filter_ui(listOfExpenses, m, undoList)
            elif m[0] == 'undo':
                undo_ui(listOfExpenses, undoList, initialList)
            elif m[0] == 'end':
                return
            else:
                raise SyntaxError('Invalid command!')
        except Exception as e:
            print(e)


'''
    Here is the initialization
'''


def testInit(listOfExpenses):
    listOfExpenses.append(createExpense('1', 50, 'housekeeping'))
    listOfExpenses.append(createExpense('2', 150, 'food'))
    listOfExpenses.append(createExpense('3', 100, 'transport'))
    listOfExpenses.append(createExpense('6', 400, 'clothing'))
    listOfExpenses.append(createExpense('6', 100, 'internet'))
    listOfExpenses.append(createExpense('9', 20, 'others'))
    listOfExpenses.append(createExpense('11', 175, 'food'))
    listOfExpenses.append(createExpense('12', 325, 'transport'))
    listOfExpenses.append(createExpense('17', 50, 'others'))
    listOfExpenses.append(createExpense('20', 100, 'housekeeping'))




