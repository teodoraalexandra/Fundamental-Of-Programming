'''
Dynamic programming
1. overlapping subproblems
2. memoization
3. principle of optimality

Greedy is applicable to problems for which the general
optimum is obtained from partial (local) optima
Dynamic programming is applicable to problems in which
the general optimum implies partial optima.
'''

d = {}
d[0] = 0
d[1] = 1

def f(n):
    if n not in d.keys():
        d[n] = f(n-2) + f(n-1)
    return d[n]

print(f(6))

#f(n) = f(n-2) + f(n-1)