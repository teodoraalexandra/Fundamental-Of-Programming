# Checkerboard problem

from texttable import Texttable
from random import randint
M = [[0 for i in range(8)] for j in range(8)]

for i in range(8):
    for j in range(8):
        M[i][j] = randint(0, 5)

t = Texttable()
for row in M:
    t.add_row(row)

print(t.draw())
