from repository.CarTextFileRepo import CarTextFileRepo
from domain.Car import Car

def readSettings():
    settings = {}

    f = open("car.txt",'r')
    s = f.read()

    lines = s.split("\n")

    for line in lines:
        tokens = line.split(",")
        settings[tokens[0].strip()] = tokens[0]


    print(lines)
    f.close()

    return settings

settings = readSettings()

#carRepo = None

'''
if settings["repo_type"] == "memory":
    carRepo = Repository()

elif settings["repo_type"] == "text":
    carRepo = CarTextFileRepo(settings["repo_file"])
'''



'''
class Person():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

class Student():
    pass

p1 = Person('Alice')
print(p1.name)

print(type(p1))

'''