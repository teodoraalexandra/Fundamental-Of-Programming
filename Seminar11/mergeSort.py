'''
*********************
      SORTING
*********************
'''


def mergeSort(data):
    if len(data) == 1:
        return data

    m = len(data) // 2
    left = mergeSort(data[:m])
    right = mergeSort(data[m:])

    return merge(left, right)


def merge(left, right):
    res = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    if l < len(left):
        res += left[l:]
    if r < len(right):
        res += right[r:]

    return res


import random

length = 10000

data = list(range(10))
random.shuffle(data)
print(mergeSort(data))