


class Grade:
    """
    Instances of this class represent grades as disciplineID, studentID, grade_value
    """
    def __init__(self, disciplineID, studentID, grade):
        '''
        Constructor for the Grade class
        '''
        try:
            disciplineID = int(disciplineID)
            studentID = int(studentID)
            grade = int(grade)
        except Exception:
            raise ValueError("Error: Invalid id's / grade!")
        if grade < 0 or grade > 10:
            raise ValueError('Error: Invalid grade! Needs to be between 0 and 10.')
        self._disciplineID = disciplineID
        self._studentID = studentID
        self._grade = grade

    def __eq__(self,grade):
        return self._disciplineID == grade._disciplineID and self._studentID == grade._studentID and self._grade == grade._grade

    def getDiscID(self):
        return self._disciplineID

    def getStudID(self):
        return self._studentID

    def getGrade(self):
        return self._grade

    def __str__(self):
        return str(self._disciplineID) + " " + str(self._studentID) + " " + str(self._grade)


def testGrade():
    grade  = Grade(1,2,3)
    assert str(grade) == "1 2 3"
    assert not (Grade(1,2,3) == Grade(3,2,1))

testGrade()