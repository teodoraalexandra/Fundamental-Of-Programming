from domain import *

def checkName(name, listOfFestivals):
    for festival in listOfFestivals:
        if getName(festival) == name:
            return True
    return False

def add(festival, listOfFestivals):
    '''
    INPUT: - the festival 
           - the list of festivals where we want to add the festival
    OUTPUT: the festival is added in the list of festivals
    '''
    listOfFestivals.append(festival)

def showSpring(listOfFestivals):
    list = []
    for festival in listOfFestivals:
        if getMonth(festival) == 3 or getMonth(festival) == 4 or getMonth(festival) == 5:
            list.append(festival)

    list.sort(key=getMonth)
    list.sort(key=getName)
    return list

def showSummer(listOfFestivals):
    list = []
    for festival in listOfFestivals:
        if getMonth(festival) == 6 or getMonth(festival) == 7 or getMonth(festival) == 8:
            list.append(festival)

    list.sort(key=getMonth)
    list.sort(key=getName)
    return list

def showAutumn(listOfFestivals):
    list = []
    for festival in listOfFestivals:
        if getMonth(festival) == 9 or getMonth(festival) == 10 or getMonth(festival) == 11:
            list.append(festival)

    list.sort(key=getMonth)
    list.sort(key=getName)
    return list

def showWinter(listOfFestivals):
    list = []
    for festival in listOfFestivals:
        if getMonth(festival) == 12 or getMonth(festival) == 1 or getMonth(festival) == 2:
            list.append(festival)

    list.sort(key=getMonth)
    list.sort(key=getName)
    return list

def showArtist(artist, listOfFestivals):
    '''
    INPUT: the artist
    OUTPUT: a list with all festivals where the given artist perform
    This function will take all festivals and will check where this artist perform
    If a festival is found, it will be added to the list
    '''
    list = []
    for festival in listOfFestivals:
        for a in getListOfArtists(festival):
            if a == artist:
                list.append(festival)
    return list

def testAdd():
    list = []
    festival1 = createFestival('Festival1', 2, 500, ['Eminem, Rihanna'])
    add(festival1, list)
    assert len(list) == 1
    festival2 = createFestival('Festival2', 3, 300, ['CTC'])
    add(festival2, list)
    assert len(list) == 2

def testShowArtist():
    list = []
    list.append(createFestival("Untold", 8, 500, ["Eminem", "Rihanna"]))
    list.append(createFestival("Electric", 7, 400, ['CTC', "Cedry2k"]))
    assert len(list) == 2
    artist = "Eminem"
    assert len(showArtist(artist, list)) == 1


testAdd()
testShowArtist()


