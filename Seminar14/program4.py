s1 = "monday"
s2 = "tuesday"

# s1 = "xmondayy"
# s2 = "monday"

# s1 -> s2
# possible operations:
#       -char insert
#       -char remove
#       -char replace

# s1 -> s2


def edit(s1, s2):  #T(n) belongs to O(3^n)
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if s1[-1] == s2[-1]:
        return 0 + edit(s1[:-1], s2[:-1])
    return 1 + min(edit(s1[:-1], s2[:-1]), edit(s1[:-1], s2), edit(s1, s2[:-1]))


print(edit(s1, s2))


n = len(s1)
m = len(s2)
#build T - (n+1) x (m+1) table

# O(n*m)
for i in range(n+1):
    for j in range(m+1):
        if i == 0:
            T[i][j] = j
        if j == 0:
            T[i][j] = i
        if s1[i] == s2[j]:
            T[i][j] = T[i-1][j-1]
        else:
            T[i][j] = 1 + min(T[i-1][j-1], T[i-1][j], T[i][j-1])
