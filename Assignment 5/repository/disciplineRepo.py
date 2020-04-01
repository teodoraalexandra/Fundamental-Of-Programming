from domain.discipline import Discipline
from repository.IterableStructure import IterableStructure

class DisciplineRepository:

    def __init__(self):
        self.__data = IterableStructure()

    def __len__(self):
        return len(self.__data)

    def __str__(self):
        r = ""
        for discipline in self.__data:
            r += str(discipline) + "\n"

        return r

    def initList(self):
        self.__data.append(Discipline(101, 'Logica'))
        self.__data.append(Discipline(102, 'Analiza'))
        self.__data.append(Discipline(103, 'Algebra'))
        self.__data.append(Discipline(104, 'Geometrie'))
        self.__data.append(Discipline(105, 'Programare'))
        self.__data.append(Discipline(106, 'Sport'))
        self.__data.append(Discipline(107, 'Psihologie'))
        self.__data.append(Discipline(108, 'Biologie'))
        self.__data.append(Discipline(109, 'Geografie'))
        self.__data.append(Discipline(110, 'Istorie'))

    def add(self, discipline):
        '''
        INPUT: a discipline
        OUTPUT: the discipline is added to the data base of disciplines
        '''
        self.__data.append(discipline)

    def update(self, oldDiscipline, newDiscipline):
        '''
        INPUT: the old discipline and the new discipline
        OUTPUT: the old discipline is replaced by the new discipline in the data base of disciplines
        Exception: if the discipline does not exits
        '''
        aux = []
        found = 0
        for i in range(0, len(self.__data)):
            if not (self.get(i) == oldDiscipline):
                aux.append(self.__data[i])
            else:
                found = 1
                aux.append(newDiscipline)
        if not found:
            raise ValueError('The discipline was not found')
        self.__data = aux

    def find(self, discipline):
        '''
        INPUT: a discipline
        OUTPUT: i (position) where the discipline was found
                -1 if the discipline does not exist in the data base
        '''
        for i in range(0, len(self.__data)):
            if self.__data[i] == discipline:
                return i
        return -1

    def findByID(self, id):
        '''
        INPUT: the id of the discipline
        OUTPUT: the name of the discipline with the given id
        Exception: if the discipline does not exist
        '''
        for i in self.__data:
            if i.getID() == id:
                return i.getName()
        raise ValueError("The discipline was not found")

    def get(self, index):
        '''
        INPUT: index (representing a position)
        OUTPUT: the discipline which is at the position 'index'
        Exception: if the index is not in the interval [0, length of data base]
        '''
        if index < 0 or index >= len(self.__data):
            raise RepositoryException("Invalid element position")
        return self.__data[index]

    def getAll(self):
        '''
        OUTPUT: return all disciplines from the data base
        '''
        return self.__data

    def remove(self, discipline):
        '''
        INPUT: a discipline
        OUTPUT: the discipline is removed from the data base
        '''
        if discipline in self.__data:
            self.__data.remove(discipline)
        else:
            raise ValueError("This discipline does not exist")

    def removeAll(self):
        '''
        OUTPUT: erase all the disciplines from the data base
        '''
        self.__data.clear()

class RepositoryException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message
