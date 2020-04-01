#create
def createExpense(day, sum, category):
    expense = [0, 1, 2]
    expense[0] = str(day)
    expense[1] = sum
    expense[2] = category
    return expense

#get
def getDay(expense):
    return int(expense[0])

def getSum(expense):
    return expense[1]

def getCategory(expense):
    return expense[2]

#transform in string
def string(list):
    for i in list:
        print('Day:',getDay(i),' Sum:',getSum(i),' Category:', getCategory(i))
