from domain.Student import Student
from random import choice, randint

class StudentDataBase:

    def __init__(self):
        '''
        Constructor for student data base class
        '''
        self._data = []

    def __len__(self):
        '''
        Returns the length of the student data base.
        '''
        return len(self._data)

    def __str__(self):
        '''
        Displays the data base
        '''
        string = ""
        for student in self._data:
            string += str(student) + "\n"
        return string
    def find(self,student):
        '''
        Searches for a student in the data base.
        Input:
            - student - the searched object
        Output:
            - Returns the position of the searched student object or -1 if it was not found
        '''
        for i in range(0,len(self._data)):
            if self._data[i] == student:
                return i
        return -1

    def findByID(self,id):
        for i in self._data:
            if i.getID() == id:
                return i.getName()
        raise ValueError("Error: The student was not found!")
    def initList(self):
        firstName = ["mike", "john", 'joe', 'yael', 'george', 'simon', 'vincent', 'johann', 'gilbert']
        lastName = ['walker', 'white', 'austin', 'robertson','ortega','armstrong','avila','thomas','mclain']
        for i in range(0,10):
            student = Student(randint(0,100), choice(firstName) + " " + choice(lastName))
            self._data.append(student)
    def add(self,student):
        '''
        Adds a student to the student repository
        '''
        self._data.append(student)

    def remove(self,student):
        '''
        Erases from the data base the student with the specified position
        '''

        try:
            self._data.remove(student)
        except Exception as exc:
            print(exc)

    def removeList(self):
        '''
        Erases all the entries in the data base
        '''
        self._data.clear()

    def get(self,index):
        '''
        Returns the student located at the specified index
        '''
        return self._data[index]

    def getList(self):
        """
        Returns all data base list
        """
        return self._data

    def update(self,oldStudent, newStudent):
        '''
        Updates the first occurence of oldStudent with newStudent
        Input:
            - oldStudent - the student that needs to be updated
            - newStudent - the student with which we want to update oldStudent
        '''
        aux = []
        found = 0
        for i in range(0, len(self._data)):
            if not (self.get(i) == oldStudent):
                aux.append(self._data[i])
            else:
                found = 1
                aux.append(newStudent)
        if not found:
            raise ValueError("Error: The student was not found in the list!")
        self._data = aux

'''
def testStudentDB():
    studentData = StudentDataBase()
    testDB=[Student(1,"Tudor Covaci"), Student(2,"Mike Tyson"),Student(12,"John Smith")]
    for i in range(0,len(testDB)):
        studentData.add(testDB[i])
        assert studentData.get(i) == testDB[i]
    assert len(studentData) == 3
    studentData.remove(testDB[2])
    assert len(studentData) == 2
    studentData.remove(testDB[1])
    assert str(studentData) == "1  Tudor Covaci\n"

testStudentDB()
'''