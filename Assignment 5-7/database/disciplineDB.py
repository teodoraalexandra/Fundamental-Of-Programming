from domain.Discipline import Discipline


class DisciplineDataBase:
    def __init__(self):
        '''
        Constructor for discipline data base class
        '''
        self._data = []

    def __str__(self):
        '''
        String form of discipline-type objects
        '''
        string = ""
        for discipline in self._data:
            string+=str(discipline) + "\n"
        return string

    def __len__(self):
        '''
        Provides the length of the data base
        '''
        return len(self._data)

    def add(self,discipline):
        '''
        Adds a new discipline to the data base
        Input:
            - discipline - the object that we want to add
        '''
        self._data.append(discipline)

    def remove(self,discipline):
        '''
        Removes the discipline that is located at the specified index
        Input:
            - index - the index of the object we want to be removed
        '''
        try:
            self._data.remove(discipline)
        except Exception:
            raise ValueError("The discipline was not found in the list!")

    def update(self, oldDiscipline, newDiscipline):
        '''
        Updates the first occurence of oldDiscipline with newDiscipline
        Input:
            - oldStudent - the student that needs to be updated
            - newStudent - the student with which we want to update oldStudent
        '''
        aux = []
        found = 0
        for i in range(0, len(self._data)):
            if not (self.get(i) == oldDiscipline):
                aux.append(self._data[i])
            else:
                found = 1
                aux.append(newDiscipline)
        if not found:
            raise ValueError("Error: The student was not found in the list!")
        self._data = aux

    def find(self,discipline):
        '''
        Searches for the given discipline in the data base
        Input:
             - discipline - the discipline searched for
        '''
        for index in range(0,len(self._data)):
            if self._data[index] == discipline:
                return index
        return -1
    def findByID(self,id):
        for i in self._data:
            if i.getID() == id:
                return i.getName()
        raise ValueError("Error: The discipline was not found!")
    def removeList(self):
        '''
        Clears the data base
        '''
        self._data.clear()

    def get(self,index):
        '''
        Returns the student that is at the specified index in the list
        Input:
            - index - the index of the wanted student
        '''
        if index < 0 or index > len(self._data):
            raise ValueError("Error: Invalid index!")
        return self._data[index]

    def getList(self):
        '''
        Returns the whole data base
        '''
        return self._data

def testDisciplineDB():
    disciplineData = DisciplineDataBase()
    testDB = [Discipline(1, "Mathematics"), Discipline(2, "computer science architecture"), Discipline(12, "computaTional LogICS")]
    for i in range(0, len(testDB)):
        disciplineData.add(testDB[i])
        assert disciplineData.get(i) == testDB[i]
    disciplineData.update(Discipline(1,"Mathematics"),Discipline(66,"English"))
    assert len(disciplineData) == 3
    disciplineData.remove(2)
    assert len(disciplineData) == 2
    disciplineData.remove(1)
    assert str(disciplineData) == "66  English\n"
'''
testDisciplineDB()
'''