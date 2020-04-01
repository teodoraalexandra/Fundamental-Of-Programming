'''
For a given natural number n find the minimal natural number m formed with the same digits.
E.g. n=3658, m=3568.
'''

'''
INPUT: -number x
OUTPUT: -the list of number x digits
'''
def createList(x):
    l = []
    while x > 0:
        l.append(x % 10)
        x = x // 10
    return l 

'''
INPUT: -list a
OUTPUT: -how many zeros are in list a
'''
def verifyIfZero(a):
    c = 0
    for i in range(0, len(a)):
        if a[i] == 0:
            c = c + 1
    return c

'''
INPUT: -list a
OUTPUT: -ordered list a with the zeros
'''
def inverseZero(a):
    x = verifyIfZero(a)
    a[0]=a[x]
    a[x]= 0

'''
INPUT: -list a
OUTPUT: -number
'''
def listToNumber(a):
    x = 0
    for i in range(0, len(a)):
        x = x*10 + a[i]
    return x  
    
def main():
    n = int(input('Enter a number: '))   #read the integer
    l = createList(n)   
    l.sort()   #sort method help us to sort the elements of the list
    if verifyIfZero(l) == 0:
        print(listToNumber(l))   #we print the elements of the list on the same line
    else:
        inverseZero(l)
        print(listToNumber(l)) #we print the elements of the list on the same line

main()
    
