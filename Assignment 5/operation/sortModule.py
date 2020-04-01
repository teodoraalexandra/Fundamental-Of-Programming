from domain.student import Student

def getKey(list, key):
    return list[key-1]

def key_ids(s):
    return s.getStudentId()

def key_idd(d):
    return d.getDisciplineId()

def key_name(s):
    return s.getName()

def key_name_average(s):
    list = s[0]
    return list.getName()

def key_average(s):
    return s[1]

def gnomeSort(listToBeSorted, key = lambda x: x):
    n = len(listToBeSorted)

    index = 0
    while index < n:
        if index == 0:
            index = index + 1

        if key((listToBeSorted[index])) >= key((listToBeSorted[index-1])):
            index = index + 1
        else:
            listToBeSorted[index], listToBeSorted[index - 1] = listToBeSorted[index - 1], listToBeSorted[index]
            index = index - 1

    return listToBeSorted



