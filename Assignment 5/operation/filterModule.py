def greater(item, i):
    return i < item

def partString(a, b):
    return a.lower() in b.lower()

def filter(lista, item, functie):
    '''
    Equivalent to:
    item for item in lista if functie(item)
    '''
    filteredList = []

    for i in lista:
        if functie(item, i) == True:
            filteredList.append(i)
    return filteredList







