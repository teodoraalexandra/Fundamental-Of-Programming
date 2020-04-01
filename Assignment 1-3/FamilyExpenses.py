'''
FAMILY EXPENSES
- DAY of the month (1-30)
- MONEY (positive integer)
- EXPENSE TYPE (housekeeping, food, transport, clothing, internet, others)

1. Add a new expense into the list
    add <sum><category>
    insert <day><sum><category>

2. Modify expenses from the list
    remove <day>
    remove <start day> to <end day>
    remove <category>

3. Write the expenses having different properties
    list
    list <category>
    list <caegory> [<|=|>] <value>
'''

'''
    Expenses functions
'''
import datetime
now = datetime.datetime.now()

def createExpense(day, sum, category):
    expense = [0, 1, 2]
    expense[0] = str(day)
    expense[1] = sum
    expense[2] = category
    return expense

def getDay(expense):
    return int(expense[0])

def getSum(expense):
    return expense[1]

def getCategory(expense):
    return expense[2]

'''
    Application functionalities
'''
def printMenu():
    print('\n')
    print('Expenses application menu: ')
    print('   add for adding a new expense to current day')
    print('   insert for adding a new expense')
    print('   remove for removing a given expense')
    print('   list for listing expenses with a given property')
    print('   end for closing the application')
    
def insertExpense(listOfExpenses, m):
    '''
    Read the day, the sum and the type and insert to the list of expenses
    insert <day> <sum> <category>
    '''
    if len(m) != 4 :
        raise SyntaxError('You must add only day, sum and category!')
    
    a = m[1]
    if a.isnumeric() is False:
        raise SyntaxError('The day must be numeric!')
    else:
        a = int(m[1])
        if a < 1 or a > 30:
            raise ValueError('Invalid day! Give a day between 1 and 30')
    
    b = m[2]
    if b.isnumeric() is False:
        raise SyntaxError('The sum must be numeric!')
    else:
        b = int(m[2])
        if b < 0:
            raise ValueError('The sum must be positive!')
    
    c = m[3]
    if c!= "housekeeping" and c!= "food" and c!= "transport" and c!= "clothing" and c!= "internet" and c!="others":
        raise ValueError('This category does not exist!')
    
    expense = createExpense(a,b,c)
    listOfExpenses.append(expense)

def addExpense(listOfExpenses, m):
    '''
    Read the sum and the type and add to the list of expenses to current day
    add <sum> <category>
    '''
    a = now.day

    if len(m) != 3 :
        raise SyntaxError('You must add only sum and category!')
    
    b = m[1]
    if b.isnumeric() is False:
        raise SyntaxError('The sum must be numeric!')
    else:
        b = int(m[1])
        if b < 0:
            raise ValueError('The sum must be positive!')
        
    c = m[2]
    if c!= "housekeeping" and c!= "food" and c!= "transport" and c!= "clothing" and c!= "internet" and c!="others":
        raise ValueError('This category does not exist!')
    
    expense = createExpense(a,b,c)
    listOfExpenses.append(expense)
    
def removeExpense(listOfExpenses, m):
    '''
    Remove the expenses which have a given property
    remove <day>
    remove <start day> to <end day>
    remove <category>
    '''
    if len(m) == 1 or len(m) == 3 or len(m) >= 5:
        raise SyntaxError('Invalid command!')
    
    a = m[1]
    if a.isnumeric() is True:
        a = int(m[1])
        if a < 1 or a > 30:
            raise ValueError('Invalid day! Give a day between 1 and 30')
        if len(m) == 4:
            if str(m[2]) == 'to':
                b = m[3]
                if b.isnumeric() is False:
                    raise ValueError("The end day must be an integer!")
                else:
                    b = int(m[3])
                    if b < 1 or b > 30:
                        raise ValueError('Invalid day! Give a day between 1 and 30')
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
            else:
                raise SyntaxError('Invalid command!')

        elif len(m) == 2:
            n = len(listOfExpenses)
            i= 0
            while i < n:
                day = getDay(listOfExpenses[i])
                if (day == a):
                    listOfExpenses.pop(i)
                    i = i-1
                    n = n-1
                else:
                    i = i+1
                                  
    else:
        if len(m) != 2:
            raise SyntaxError('Invalid command!')
        if m[1] != "housekeeping" and m[1]!= "food" and m[1]!= "transport" and m[1]!= "clothing" and m[1]!= "internet" and m[1]!="others":
            raise ValueError('This category does not exist!')
        n = len(listOfExpenses)
        i= 0
        while i < n:
            category = getCategory(listOfExpenses[i])
            if (category == a):
                listOfExpenses.pop(i)
                i = i-1
                n = n-1
            else:
                i = i+1
                
def listExpense(listOfExpenses, m):
    '''
    List the list of expenses which have a given property
    list
    list <category>
    list <category> [ < | = | > ] <value>
    '''
    if len(m) == 2:
        if m[1] != "housekeeping" and m[1]!= "food" and m[1]!= "transport" and m[1]!= "clothing" and m[1]!= "internet" and m[1]!="others":
            raise ValueError('This category does not exist!')
        for i in listOfExpenses:
            if getCategory(i) == m[1]:
                print(i)
                
    elif len(m) == 4:
        if m[1] != "housekeeping" and m[1]!= "food" and m[1]!= "transport" and m[1]!= "clothing" and m[1]!= "internet" and m[1]!="others":
            raise ValueError('This category does not exist!')
        
        b = m[3]
        if b.isnumeric() is False:
            raise ValueError('You must introduce a numeric value for comparation')

        b = int(m[3])
        if m[2] == ">":
            for i in listOfExpenses:
                if getCategory(i) == m[1] and getSum(i) > b:
                    print(i)
        elif m[2] == "=":
            for i in listOfExpenses:
                if getCategory(i) == m[1] and getSum(i) == b:
                    print(i)
        elif m[2] == "<":
            for i in listOfExpenses:
                if getCategory(i) == m[1] and getSum(i) < b:
                    print(i)
        else:
            raise SyntaxError('Invalid command. You are allow to enter <,> or =!')
        
            
    elif len(m) == 1:
        print(*listOfExpenses, sep='\n')
        
    else:
        raise SyntaxError('Invalid syntax!')
    
def run():
    '''
        Implement user interface
    '''
    listOfExpenses = []
    testInit(listOfExpenses)
    commands = {'add': addExpense, 'insert': insertExpense, 'remove': removeExpense, 'list': listExpense}

    while True:
        printMenu()
        m = input().split(' ')

        try:
            if m[0] == 'add':
                addExpense(listOfExpenses, m)
            elif m[0] == 'insert':
                insertExpense(listOfExpenses, m)
            elif m[0] == 'remove':
                removeExpense(listOfExpenses, m)
            elif m[0] == 'list':
                listExpense(listOfExpenses, m)
            elif m[0] == 'end':
                return
            else:
                raise SyntaxError('Invalid command!')
        except Exception as e:
            print(e)

'''
    Here are the tests
'''

def testInit(listOfExpenses):
    listOfExpenses.append(createExpense('1', 50, 'housekeeping'))
    listOfExpenses.append(createExpense('2', 150, 'food'))
    listOfExpenses.append(createExpense('3', 100, 'transport'))
    listOfExpenses.append(createExpense('6', 400, 'clothing'))
    listOfExpenses.append(createExpense('6', 100, 'internet'))
    listOfExpenses.append(createExpense('9', 20, 'others'))
    listOfExpenses.append(createExpense('11', 175, 'food'))
    listOfExpenses.append(createExpense('12', 80, 'transport'))
    listOfExpenses.append(createExpense('17', 50, 'others'))
    listOfExpenses.append(createExpense('20', 100, 'housekeeping'))

run()
