def search(data, key):
    return binarySearch(data, 0, len(data)-1, key)

def binarySearch(data, left, right, key):
    m = (left+right) // 2
    if left > right:
        return -1
    if key == data[m]:
        return m
    if key < data[m]:
        return binarySearch(data, left, m, key)
    else:
        return binarySearch(data, m, right, key)
    return -1

data = list(range(10))
print(data)
print(search(data, 7))