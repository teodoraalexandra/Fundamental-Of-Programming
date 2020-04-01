
class GradeController:
    def __init__(self,db):
        self._db = db
        self._undo = []
    def __str__(self):
        return str(self._db)

    def addGrade(self,grade):
        self._undo = self._db.getList()[:]
        self._db.add(grade)

    def removeGrade(self,grade):
        self._undo = self._db.getList()[:]
        self._db.remove(grade)
    def getStudentGrades(self,studentID):
        return self._db.findGradesOfStudent(studentID)

    def getEnrolledStudents(self,disciplineID):
        return self._db.findEnrolledStudents(disciplineID)