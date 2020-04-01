#create festival
def createFestival(name, month, cost, listOfArtists):
    festival = [0, 1, 2, 3]
    festival[0] = name
    festival[1] = month
    festival[2] = cost
    festival[3] = listOfArtists
    return festival

#get
def getName(festival):
    return festival[0]

def getMonth(festival):
    return int(festival[1])

def getCost(festival):
    return int(festival[2])

def getListOfArtists(festival):
    return festival[3]

#string
def string(listOfArtists):
    for artist in listOfArtists:
        return artist

def string(festival):
    return getName(festival) + " " + str(getMonth(festival)) + " " + str(getCost(festival)) + string(getListOfArtists(festival))
