from domain import *
from functions import *

def printMenu():
    print("\n")
    print("You have the following commands available: ")
    print("     1- Add a music festival")
    print("     2- Show a festival for a given season")
    print("     3- Show all festival where a given artist will perform")
    print("     0- Exit")
    print("\n")

def add_ui(listOfFestivals):
    a = input("Enter the name of the festival:  ")
    if checkName(a, listOfFestivals):
        raise ValueError('This festival already exists.')
    b = int(input("Enter the month of the festival:  "))
    if b < 1 or b > 12:
        raise ValueError("The month is not between 1 and 12.")
    c = int(input("Enter the cost of the festival:  "))
    d = []
    lenD = int(input("How many artists do you want to add?  "))
    for i in range(0, lenD):
        artist = input("Enter artist:  ")
        d.append(artist)

    festival = createFestival(a, b, c, d)
    add(festival, listOfFestivals)

def showSeason_ui(listOfFestivals):
    season = input("Enter the season for the festivals:  ")
    if season == "spring":
        print(showSpring(listOfFestivals))
    elif season == "summer":
        print(showSummer(listOfFestivals))
    elif season == "autumn":
        print(showAutumn(listOfFestivals))
    elif season == "winter":
        print(showWinter(listOfFestivals))
    else:
        print("This season does not exist.")

def showArtist_ui(listOfFestivals):
    artist = input("Enter the name of the artist: ")
    print(showArtist(artist, listOfFestivals))

def run():
    listOfFestivals = []
    initialization(listOfFestivals)

    stop = False
    while stop == False:
        printMenu()
        command = input("Enter a command: ")
        try:
            if command == "1":
                add_ui(listOfFestivals)
            elif command == "2":
                showSeason_ui(listOfFestivals)
            elif command == "3":
                showArtist_ui(listOfFestivals)
            elif command == "0":
                stop = True
            else:
                print('Your command is invalid')
        except Exception as e:
            print(e)


def initialization(listOfFestivals):
    listOfFestivals.append(createFestival("Untold", 8, 500, ["Eminem", "Rihanna"]))
    listOfFestivals.append(createFestival("Electric", 7, 400, ['CTC', "Cedry2k"]))
    listOfFestivals.append(createFestival("SummerWave", 5, 300, ["Smiley", "Andra"]))
    listOfFestivals.append(createFestival("Tunder", 9, 800, ["Haarp Cord", "Eminem"]))
    listOfFestivals.append(createFestival("BearWorld", 12, 300, ["Eminem", "Smiley"]))

run()