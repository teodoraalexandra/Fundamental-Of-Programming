from domain import *

#add function
def addExpense(expense, listOfExpenses):
    listOfExpenses.append(expense)

#remove functions
def removeStartToEnd(listOfExpenses, a, b):
    n = len(listOfExpenses)
    i = 0
    while i < n:
        day = getDay(listOfExpenses[i])
        if (day >= a) and (day <= b):
            listOfExpenses.pop(i)
            i = i-1
            n = n-1
        else:
            i = i+1

def removeDay(listOfExpenses, a):
    n = len(listOfExpenses)
    i = 0
    while i < n:
        day = getDay(listOfExpenses[i])
        if day == a:
            listOfExpenses.pop(i)
            i = i-1
            n = n-1
        else:
            i = i+1

def removeCategory(listOfExpenses, a):
    n = len(listOfExpenses)
    i= 0
    while i < n:
        category = getCategory(listOfExpenses[i])
        if category == a:
            listOfExpenses.pop(i)
            i = i-1
            n = n-1
        else:
            i = i+1

#list functions


def listAll(listOfExpenses):
    l = []
    for i in listOfExpenses:
        l.append(i)
    return l

def listCategory(listOfExpenses, a):
    l = []
    for i in listOfExpenses:
        if getCategory(i) == a:
            l.append(i)
    return l

def listGreater(listOfExpenses, a, b):
    l = []
    for i in listOfExpenses:
        if getCategory(i) == a and getSum(i) > b:
            l.append(i)
    return l

def listEqual(listOfExpenses, a, b):
    l = []
    for i in listOfExpenses:
        if getCategory(i) == a and getSum(i) == b:
            l.append(i)
    return l

def listSmaller(listOfExpenses, a, b):
    l = []
    for i in listOfExpenses:
        if getCategory(i) == a and getSum(i) < b:
            l.append(i)
    return l

#sum, max, sort functions


def sum(listOfExpenses, a):
    total = 0
    for i in listOfExpenses:
        if getCategory(i) == a:
            total = total + getSum(i)
    return total

def max(listOfExpenses):
    max = 0
    for j in range(1, 31):
        total = 0
        for i in listOfExpenses:
            if getDay(i) == j:
                total = total + getSum(i)
        if total > max:
            max = total
            day = j
    return day

def sortCategory(listOfExpenses, a):
    listByCategory = []
    for i in listOfExpenses:
        if getCategory(i) == a:
            listByCategory.append(i)
    listByCategory.sort(key = getSum)
    return listByCategory


def sortDay(listOfExpenses, a):
    listByDay = []
    for i in listOfExpenses:
        if getDay(i) == a:
            listByDay.append(i)
    listByDay.sort(key=getSum)
    return listByDay

#filter functions

def filterCategory(listOfExpenses, a):
    filterList = []
    for i in listOfExpenses:
        if getCategory(i) == a:
            filterList.append(i)
    listOfExpenses[:] = filterList
    return listOfExpenses

def filterGreater(listOfExpenses, a, b):
    filterList = []
    for i in listOfExpenses:
        if getCategory(i) == a and getSum(i) > b:
            filterList.append(i)
    listOfExpenses[:] = filterList
    return listOfExpenses

def filterEqual(listOfExpenses, a, b):
    filterList = []
    for i in listOfExpenses:
        if getCategory(i) == a and getSum(i) == b:
            filterList.append(i)
    listOfExpenses[:] = filterList
    return listOfExpenses

def filterSmaller(listOfExpenses, a, b):
    filterList = []
    for i in listOfExpenses:
        if getCategory(i) == a and getSum(i) < b:
            filterList.append(i)
    listOfExpenses[:] = filterList
    return listOfExpenses

'''
HERE ARE THE TESTS
'''
def testAddExpense():
    listOfExpenses = []
    addExpense(createExpense('1', 500, 'food'), listOfExpenses)
    assert len(listOfExpenses) == 1 and getDay(listOfExpenses[0]) == '1' and getSum(listOfExpenses[1]) == 500 and getCategory(listOfExpenses[2]) == 'food'
    addExpense(createExpense('5', 100, 'others'), listOfExpenses)
    assert len(listOfExpenses) == 2 and getDay(listOfExpenses[0]) == '5' and getSum(listOfExpenses[1]) == 100 and getCategory(listOfExpenses[2]) == 'others'
    addExpense(createExpense('20', 50, 'transport'), listOfExpenses)
    assert len(listOfExpenses) == 3 and getDay(listOfExpenses[0]) == '20' and getSum(listOfExpenses[1]) == 50 and getCategory(listOfExpenses[2]) == 'transport'


def testRemoveExpense():
    listOfExpenses = [createExpense('1',100, 'housekeeping'), createExpense('5', 200, 'food'), createExpense('6',100,'clothing'), createExpense('7',20,'internet'), createExpense('10',200,'others'), createExpense('22', 40, 'transport')]
    removeStartToEnd(listOfExpenses, 1, 6)
    assert len(listOfExpenses) == 3
    assert getDay(listOfExpenses[0]) == '7' and getSum(listOfExpenses[0]) == 20 and getCategory(listOfExpenses[0]) == 'internet'
    assert getDay(listOfExpenses[2]) == '22' and getSum(listOfExpenses[2]) == 40 and getCategory(listOfExpenses[2]) == 'transport'
    removeCategory(listOfExpenses, 'internet')
    assert len(listOfExpenses) == 2
    assert getDay(listOfExpenses[0]) == '10' and getSum(listOfExpenses[0]) == 200 and getCategory(listOfExpenses[0]) == 'others'
    removeDay(listOfExpenses, '10')
    assert getDay(listOfExpenses[0]) == '22' and getSum(listOfExpenses[0]) == 40 and getCategory(listOfExpenses[0]) == 'transport'




