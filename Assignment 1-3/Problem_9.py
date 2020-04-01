'''
Find the smallest number m from the Fibonacci sequence, defined by f[0]=f[1]=1, f[n]=f[n1]+f[n-2],
for n>2, larger than the given natural number n. So, find k and m such that f[k]=m,
m>n and f[k-1] <=n.
'''

'''
INPUT: -an integer larger than 2 (read from keyboard)
OUTPUT: -m which is the smallest number from Fibonacci sequence
'''
def fibonacci(a):
    f1 = 1
    f2 = 1
    fib = 2
    k = 3
    
    while (fib < a):
        f1 = f2
        f2 = fib
        fib = f1 + f2
        k = k + 1
        
    m = fib
    return m

'''
INPUT: -an integer larger than 2 (read from keyboard)
OUTPUT: -m which is the smallest number from Fibonacci sequence
'''

def position(a):
    f1 = 1
    f2 = 1
    fib = 2
    k = 3

    while (fib < a):
        f1 = f2
        f2 = fib
        fib = f1 + f2
        k = k + 1

    return k

n = int(input('Enter a number larger than 2: '))
x = position(n)
y = fibonacci(n)
print('The number is f[',x,']= ',y)
    

    
