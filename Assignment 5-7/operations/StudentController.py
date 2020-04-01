from database import studentDB
class StudentController:

    def __init__(self,db):
        """
        Constructor for the StudentController class
        """
        self._db = db
        self._undo = []

    def __str__(self):
        return str(self._db)

    def addStudent(self,student):
        """
        Adds a student to the data base
        Input:
            - student - the Student class object that needs to be added
        """
        self._undo = self._db.getList()[:]
        self._db.add(student)

    def removeStudent(self, student):
        """
        Removes the student at the specified index.
        Input:
            - index - the index of the student that needs to be removed
        """
        self._undo = self._db.getList()[:]
        self._db.remove(student)
    def updateStudent(self,oldStudent,newStudent):
        """
        Updates a student.
        Input:
            - oldStudent - the student that needs to be updated
            - newStudent - the student to which oldStudent needs to be updated
        """
        self._db.update(oldStudent,newStudent)
    def removeList(self):
        """
        Erases the student data base.
        """
        self._undo = self._db.getList()[:]
        self._db.removeList()
    def findByID(self,studentID):
        return self._db.findByID(studentID)
    def getList(self):
        """
        Returns the whole student data base
        """
        return self.__db.getList()

