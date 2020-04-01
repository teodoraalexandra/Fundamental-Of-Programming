from texttable import Texttable

'''
    Divide and conquer
    1. Divide -> split the problem intro several smaller problems of the same type
    2. Conquer -> solve the small subproblems
    3. Combine -> combine the small solutions to solve the initial problem
'''

'''
    Find the minimum element in a list 
    1. Divide - split the list in two halves
    2. Conquer - determinte minimum in each half 
    3. Combine - compare the two minimums
'''

def minList(data):
    if len(data) == 1:
        return data[0]

    m = len(data) // 2

    m1 = minList(data[:m])
    m2 = minList(data[m:])
    return min(m1, m2)

'''
    Find the minimum element in a list 
    1. Divide - split the list in first element and rest of list
    2. Conquer - determine minimum of first element and rest of list
    3. Combine - compare the two minimums
'''

def minListChipConquer(data):
    if len(data) == 1:
        return data[0]

    m1 = data[0]
    m2 = minListChipConquer(data[1:])
    return min(m1, m2)


print(minListChipConquer([2, 7, 1, 5, -1, 5, 2, 3, 3, 6, 9]))

'''
Sum of elements on positions that are multiples of 3
2, 7, 1, 5, -1, 5, 2, 3, 3, 6, 9
x        x         x        x     = 15
'''

def sumList(data):
    if len(data) <= 3:
        return data[0]

    return data[0] + sumList(data[3:])

print(sumList([2, 7, 1, 5, -1, 5, 2, 3, 3, 6, 9]))

'''
Determine the r-th root for given number n with precision p 
given: n, r, p
find: x

n = 2
r = 10
p = 0.01
x = ?

1.99 <= x^r <= 2.01
We will take the [1,n] interval
'''

def root(n, r, p):
    if n >=1:
        return rootInternal(n, r, p, 0, n)
    else:
        return rootInternal(n, r, p, n, 1)

def rootInternal(n, r, p, left, right):
    m = (left + right) / 2
    if abs(m ** r - n) < p:
        return m

    if m**r < n:
        return rootInternal(n, r, p, m, right)
    else:
        return rootInternal(n, r, p, left, m)


p = 0.1
print(root(0.2, 2, 0.001),' ',root(0.2, 2, 0.001)**2)

'''
for i in range(8):
    print(root(1, 3, 0.1),' ', root(1, 3, p)**2)
    p /= 10
'''


'''
    BKT
    1. Search space representation
    2. consistent(x) -> can we reach a solution by only adding values to x ?
    3. solution(x) -> is array x a solution ?
'''


def consistent(x):
    if len(x) == len(set(x)):
        return False
    for i in range(len(x) - 1):
        if abs(x[-1] - x[i]) == len(x) - i - 1:
            return False

    return True


def solution(x, n):
    return len(x) == n


def solutionFound(x, n):
    #print(x)
    t = Texttable()
    for i in x:
        row = [""]*n
        row[i] = 'R'
        t.add_row(row)
    print(t.draw())
    print("\n")


def backtrackIterative(n):
    x = [-1]
    while len(x) > 0:
        chosen = False
        while not chosen and x[len(x) - 1] < n-1:
            x[len(x) - 1] += 1
            chosen = consistent(x)
        if chosen:
            if solution(x, n):
                solutionFound(x, n)
            else:
                x.append(-1)
        else:
            x = x[:-1]

backtrackIterative(5)

