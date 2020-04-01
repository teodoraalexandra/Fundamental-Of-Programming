def consistent(lst):
    m = 0
    for i in lst:
        m += listCoins[i]
    if m <= s:
        return True
    return False


def solution(lst):
    m = 0
    for i in lst:
        m += listCoins[i]
    if m == s:
        return True
    return False


def solutionFound(lst):
    print("The possible combinations of coins are: ")
    res = []
    for i in lst:
        res.append(listCoins[i])
    print(res)
    print(" ")


def backtrackingIterative(n):
    lst = [-1]
    ok = True
    while len(lst) > 0:
        chosen = False
        while not chosen and lst[len(lst) - 1] < n - 1:
            lst[len(lst) - 1] += 1
            chosen = consistent(lst)
        if chosen:
            if solution(lst):
                ok = False
                solutionFound(lst)
            else:
                lst.append(-1)

        else:
            lst = lst[:-1]

    if ok:
        print("No possible combinations.")


def backtrackingRecursive(lst, var):
    lst.append(0)
    ok = True
    for i in range(0, n):
        lst[-1] = i
        if consistent(lst):
            if solution(lst):
                ok = False
                solutionFound(lst)
                var += 1
            backtrackingRecursive(lst, var)
    lst.pop()
    return var

'''
MENU
r - recursive
i - iterative
'''
option = str(input("Press r for recursive or i for iterative: "))
if option == "r":
    n = int(input("Enter the number of coins: "))
    listCoins = []

    for i in range(1, n+1):
        a = int(input("Coin " + str(i) + "= "))
        listCoins.append(a)
    var = 0
    s = int(input("Enter the sum: "))
    if backtrackingRecursive([], var) == 0:
        print("No possible combinations.")


elif option == "i":
    n = int(input("Enter the number of coins: "))
    listCoins = []

    for i in range(1, n + 1):
        a = int(input("Coin " + str(i) + " = "))
        listCoins.append(a)
    var = 0
    s = int(input("Enter the sum: "))
    backtrackingIterative(n)

else:
    print("Try again...")

