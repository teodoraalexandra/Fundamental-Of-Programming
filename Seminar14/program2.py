# knapsack problem
w = 10
values = [4, 1, 2, 4, 2]
weights = [3, 3, 2, 3, 4]


# 1. items can be divided
# 2. item cannot be divided (0-1 knapsack problem)

# d1 -> d2 -> d3 -> d4

# I am on the n-th object right now

def knapsack(w, values, weights, n):  # T(n) belongs to O()
    if n < 0:
        return 0
    if weights[n] > w:
        return knapsack(w, values, weights, n - 1)
    return max(knapsack(w, values, weights, n - 1), values[n] + knapsack(w-weights[n], values, weights, n-1))


from texttable import Texttable


def prettyPrint(T):
    tbl = Texttable()
    tbl.header([''] + list(range(len(T[0]))))
    for i in range(len(T)):
        tbl.add_row([i] + T[i])
    print(tbl.draw())


def knapsack_dp(w, values, weights):  # O(n * w)
    n = len(values)
    T = [[0 for i in range(w+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                T[i][j] = 0
            elif weights[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j], values[i-1] + T[i-1][j - weights[i-1]])
    prettyPrint(T)
    return T[n][w]


print(knapsack(w, values, weights, len(values)-1))
print(knapsack_dp(w, values, weights))
