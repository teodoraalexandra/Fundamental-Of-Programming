'''
Determine the n-th elements of the sequence 1,2,3,2,5,2,3,7,2,3,2,5,... obtained from the
sequence of natural numbers by replacing composed numbers with their prime divisors,
without memorizing the elements of the sequence.
'''

'''
Input: an integer a
Output: -TRUE if the integer is prime
        -FALSE, otherwise
'''

def isPrime(a):
    if a <= 1:
        return False
    if a == 2:
        return True
    for i in range(2, a):   #from 2 to a we check every number to see if it is a possible divisor
        if (a % i == 0):
            return False   #if we find a divisor, the number is not prime
    return True

'''
Input: -n: the number from which we want to get the next prime divisor
       -d: the divizor which is smaller than the next divizor, we start
           from this one
Output: the next prime divisor of the number if that exists and it is
        smaller than the number
    ELSE: return -1 when there is no such divisor for our number
'''
def nextPrimeDiv(n, d):
    next = d + 1
    while (isPrime(next) == False or n % next != 0) and next <= n:
        next = next + 1
    if next <= n:
        return next
    else:
        return -1

'''
Input: -n: integer. We generate the n-th number of the sequence
Output: the value of the n-th element
'''
def generateTheNthElementOfTheSequence(k):
    number = 2
    element = 1
    if k == 1:
        return 1
    else:
        k = k-1
    while k:
        while element != -1 and k and element <= number:
            element = nextPrimeDiv(number, element)
            if element != -1:
                k = k - 1
            if k == 0:
                return element

        number = number + 1
        element = 1
            
    
def main():
    n = int(input('Enter a number: '))  
    print('The n-th element is: ',generateTheNthElementOfTheSequence(n))


main()




