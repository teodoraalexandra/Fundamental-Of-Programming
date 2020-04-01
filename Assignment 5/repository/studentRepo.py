from domain.student import Student
from repository.IterableStructure import IterableStructure
from random import choice

class StudentRepository:

    def __init__(self):
        self.__data = IterableStructure()

    def __len__(self):
        return len(self.__data)

    def __str__(self):
        r = ""
        for student in self.__data:
            r += str(student) + "\n"

        return r

    def initList(self):
        name = ['Teodora', 'Bianca', 'Tudor', 'Mara', 'Vlad', 'Ioana', 'Amalia', 'Doru', 'Radu', 'Mircea']
        for i in range(1, 101):
            self.__data.append(Student(i, choice(name)))

    def add(self, student):
        '''
        INPUT: a student
        OUTPUT: the student is added to the data base of students
        '''
        self.__data.append(student)

    def update(self, oldStudent, newStudent):
        '''
        INPUT: the old student and the new student
        OUTPUT: the old student is replaced by the new student in the data base of students
        Exception: if the student does not exits
        '''
        aux = []
        found = 0
        for i in range(0, len(self.__data)):
            if not (self.get(i) == oldStudent):
                aux.append(self.__data[i])
            else:
                found = 1
                aux.append(newStudent)
        if not found:
            raise ValueError('The student was not found')
        self.__data = aux

    def find(self, student):
        '''
        INPUT: a student
        OUTPUT: i (position) where the student was found
                -1 if the student does not exist in the data base
        '''
        for i in range(0, len(self.__data)):
            if self.__data[i] == student:
                return i
        return -1

    def findByID(self, id):
        '''
        INPUT: the id of the student
        OUTPUT: the name of the student with the given id
        Exception: if the student does not exist
        '''
        for i in self.__data:
            if i.getID() == id:
                return i.getName()
        raise ValueError("The student was not found")

    def get(self, index):
        '''
        INPUT: index (representing a position)
        OUTPUT: the student which is at the position 'index'
        Exception: if the index is not in the interval [0, length of data base]
        '''
        if index < 0 or index >= len(self.__data):
            raise RepositoryException("Invalid element position")
        return self.__data[index]

    def getAll(self):
        '''
        OUTPUT: return all students from the data base
        '''
        return self.__data

    def remove(self, student):
        '''
        INPUT: a student
        OUTPUT: the student is removed from the data base
        '''
        if student in self.__data:
            self.__data.remove(student)
        else:
            raise ValueError("This student does not exist")

    def removeAll(self):
        '''
        OUTPUT: erase all the students from the data base
        '''
        self.__data.clear()

class RepositoryException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message


