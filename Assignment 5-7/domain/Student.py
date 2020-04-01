class Student:
    """
    Instances of this class represent a student by studentID and name
    """
    def __init__(self,studentID,name):
        """
        Constructor for the Student class
        Input:
            - ID - the id of the student
            - name - the name of the student
        """
        try:
            studentID = int(studentID)
        except Exception:
            raise ValueError("The ID needs to be an integer")
        for i in range(0,len(name)):
            if name[i].isdigit() is True:
                raise ValueError("The name needs to be a string without numbers!")
        splitName = name.split()
        name = ""
        for i in splitName:
            i = i.capitalize()
            name = name + i + " "
        name = name[:-1]
        self._ID = studentID
        self._name = name

    def __str__(self):
        return "%-10s"%str(self._ID) + "%-16s"%self._name

    def __eq__(self,student):
        return self._ID == student._ID and self._name == student._name

    def getID(self):
        return self._ID

    def getName(self):
        return self._name

    def setID(self,newID):
        self._ID = newID

    def setName(self,newName):
        self._name = newName
'''
def testStudent():

    assert str(Student(1, "Tudor")) == "1  Tudor"
    assert Student(1, "Tudor") == Student(1, "Tudor")
    assert Student(1, "Tudor Covaci") == Student(1, "Tudor Covaci")
    assert Student(1, "tudor") == Student(1, "Tudor")
    assert str(Student(12,"CovAci TudOR")) == "12  Covaci Tudor"
    student1 = Student(12,"TuDOr CoVAci")
    assert student1._name == "Tudor Covaci"

'''
#testStudent()