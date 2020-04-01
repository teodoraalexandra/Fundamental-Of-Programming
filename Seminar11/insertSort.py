def insertSort(data):
    for i in range(1, len(data)):
        el = data[i]
        j = i - 1
        while j >= 0 and data[j] > el:
            data[j+1] = data[j]
            j -= 1
        data[j+1]
    return data

import random

length = 10000

data = list(range(10))
random.shuffle(data)
print(insertSort(data))