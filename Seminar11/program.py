'''
*********************
       LOOPS
*********************

n = input size
T(n) = nr. of operations
T(n) = sum*from 1 to n* of 1 = n


BestCase, AverageCase, WorstCase
BC: T(n) = 1 (the element is the first)
WC: T(n) = n (the element is the last)
AC: T(n) = (1+2+...+n)/n = (n+1)/2

*********************
    NESTED LOOPS
*********************

T(n) = sum*from 1 to n^2* of i = (1+2+...+n^2) = (n^2)(n^2+1)/2

'''
def f(data):
    '''
    constant time
    '''
    return 1

def f(data, data2):
    '''
    constant time
    '''
    wait_one_day
    return 1

def f(data):
    '''
    constant time
    '''
    for i in range(5): <-5 operations x 2 = 10 operations
        print(i) <- 1 operation
        i += 1 <- 1 operation

