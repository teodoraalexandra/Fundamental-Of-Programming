from domain.Grade import Grade
from database import studentDB
from database import disciplineDB
from random import randint,choice
class GradeDataBase:
    def __init__(self):
        """
        Constructor for grade data base class
        """
        self._data = []

    def __str__(self):
        """
        String format of the grade data base
        """
        string = ""
        for grade in self._data:
            string += str(grade) + "\n"
        return string

    def __len__(self):
        """
        Returns the length of the grade data base
        """
        return self._data

    def initList(self,studentDB,disciplineDB):
        studentIDs = []
        disciplineIDs = []
        for i in studentDB.getList():
            studentIDs.append(i.getID())
        for i in disciplineDB.getList():
            disciplineIDs.append(i.getID())
        for i in range(0,10):
            grade = Grade(choice(disciplineIDs),choice(studentIDs),randint(0,10))
            self._data.append(grade)
    def add(self,grade):
        """
        Adds a grade to the grade data base.
        Input:
            - grade - the grade that needs to be added
        """
        self._data.append(grade)

    def remove(self,grade):
        """
        Removes the object located at the specified index in the data base
        Input:
             - index - the index of the object that needs to be removed
        """
        try:
            self._data.remove(grade)
        except Exception:
            raise ValueError("The grade was not found in the list!")

    def removeAll(self):
        """
        Clears the data base
        """
        self._data.clear()

    def get(self,index):
        """
        Returns the grade that is placed at the given index
        Input:
            - index - the index of the wanted grade
        """
        return self._data[index]

    def findGradesOfStudent(self,studentID):
        listOfGrades = []
        for i in self._data:
            if i.getStudID() == studentID:
                listOfGrades.append(i)
        return listOfGrades

    def findEnrolledStudents(self,disciplineID):
        listOfStudents = []
        for i in self._data:
            if i.getDiscID() == disciplineID:
                listOfStudents.append(i)
        return listOfStudents
    def getList(self):
        """
        Returns the whole data base.
        """
        return self._data


