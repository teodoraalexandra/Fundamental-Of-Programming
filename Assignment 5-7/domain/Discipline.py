class Discipline:
    """
    Instances of this class represent disciplines by disciplineID and name.
    """

    def __init__(self, disciplineID,name):
        try:
            disciplineID = int(disciplineID)
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
        self._ID = disciplineID
        self._name = name

    def __str__(self):
        return "%-10s" % str(self._ID) + "%-16s" % self._name

    def __eq__(self,discipline):
        return self._ID == discipline._ID and self._name ==discipline._name

    def getID(self):
        return self._ID
    def getName(self):
        return self._name
    def setID(self,newID):
        self._ID = newID
    def setName(self,newName):
        self._name = newName
'''
def testDiscipline():

    assert str(Discipline(1,"maThematics")) == "1  Mathematics"
    assert str(Discipline(12,"COmpuTer SysTEMs arcHIteCTUre")) == "12  Computer Systems Architecture"
    assert Discipline(12, "ComputER SysTEMs arcHIteCTUre") == Discipline(12,"computer systems architecture")

testDiscipline()
'''