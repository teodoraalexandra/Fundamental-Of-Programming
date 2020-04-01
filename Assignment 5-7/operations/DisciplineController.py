from database import disciplineDB
class DisciplineController:

    def __init__(self,db):
        """
        Constructor for the DisciplineController class
        """
        self._db = db
        self._undo = []

    def __str__(self):
        return str(self._db)

    def addDiscipline(self,discipline):
        """
        Adds a discipline to the data base
        Input:
            - discipline - the Discipline class object that needs to be added
        """
        self._undo = self._db.getList()[:]
        self._db.add(discipline)

    def removeDiscipline(self, discipline):
        """
        Removes the specified discipline from the data base
        Input:
            - discipline - the discipline that needs to be removed
        """
        self._undo = self._db.getList()[:]
        self._db.remove(discipline)
    def updateDiscipline(self,oldDiscipline,newDiscipline):
        """
        Updates a discipline.
        Input:
            - oldDiscipline - the student that needs to be updated
            - newDiscipline - the student to which oldStudent needs to be updated
        """
        self._db.update(oldDiscipline,newDiscipline)

    def removeList(self):
        """
        Erases the discipline data base.
        """
        self._undo = self._db.getList()[:]
        self._db.removeList()

    def findByID(self,id):
        return self._db.findByID(id)

    def getList(self):
        """
        Returns the whole discipline data base
        """
        return self.__db.getList()

