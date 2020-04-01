from domain.grade import Grade
from domain.discipline import Discipline
from domain.student import Student
from repository.studentRepo import StudentRepository
from repository.disciplineRepo import DisciplineRepository
from random import randint
from repository.IterableStructure import IterableStructure

class GradeRepository:

    def __init__(self):
        self.__data = IterableStructure()

    def __str__(self):
        r = ""
        for grade in self.__data:
            r += str(grade) + "\n"

        return r

    def __len__(self):
        return len(self.__data)

    def initList(self):
        for i in range(1, 101):
            self.__data.append(Grade(randint(101, 110), randint(1, 100), randint(1, 10)))

    def add(self, grade):
        '''
        INPUT: a grade
        OUTPUT: the grade is added to the data base of grades
        '''
        self.__data.append(grade)

    def remove(self, grade):
        '''
        INPUT: a grade
        OUTPUT: the grade is removed from the data base
        '''
        self.__data.remove(grade)

    def removeAll(self):
        '''
        OUTPUT: erase all the grades from the data base
        '''
        self.__data.clear()

    def get(self, index):
        '''
        INPUT: index (representing a position)
        OUTPUT: the grade which is at the position 'index'
        Exception: if the index is not in the interval [0, length of data base]
        '''
        if index < 0 or index >= len(self.__data):
            raise RepositoryException("Invalid element position")
        return self.__data[index]


    def getAll(self):
        '''
        OUTPUT: return all grades from the data base
        '''
        return self.__data

    def findGradesOfStudent(self, studentId):
        '''
        INPUT: the student id
        OUTPUT: all grades of the student which has the given id
        '''
        listOfGrades = []
        for i in self.__data:
            if i.getStudentId() == studentId:
                listOfGrades.append(i)
        return listOfGrades

    def getEnrolledStudents(self, disciplineId):
        '''
        INPUT: the discipline id
        OUTPUT: all students which are enrolled at the discipline which has the given id
        '''
        listOfStudents = []
        for i in self.__data:
            if i.getDisciplineId() == disciplineId:
                listOfStudents.append(i)
        return listOfStudents

    def getGrades(self, ID):
        '''
        INPUT: an id (either of a student or a discipline)
        OUTPUT: all grades of the student which has the given id OR
                all grades which exist at a given discipline
        '''
        listOfGrades = []
        for i in self.__data:
            if i.getStudentId() == ID or i.getDisciplineId() == ID:
                listOfGrades.append(i.getValue())

        return listOfGrades

class RepositoryException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message
