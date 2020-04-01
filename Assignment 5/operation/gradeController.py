from repository.disciplineRepo import DisciplineRepository
from repository.studentRepo import StudentRepository
from random import randint
from domain.grade import Grade
class GradeController:
    def __init__(self, repoG, repoS, repoD):
        self.__repoG = repoG
        self.__repoS = repoS
        self.__repoD = repoD

    def __str__(self):
        return str(self.__repoG)

    def addGrade(self, grade):
        self.__undo = self.__repoG.getAll()[:]
        self.__repoG.add(grade)

    def removeGrade(self, grade):
        self.__undo = self.__repoG.getAll()[:]
        self.__repoG.remove(grade)

    def getStudentGrades(self, studentId):
        return self.__repoG.findGradesOfStudent(studentId)

    def getEnrolledStudents(self, disciplineId):
        return self.__repoG.getEnrolledStudents(disciplineId)

    def getGrades(self, ID):
        return self.__repoG.getGrades(ID)

    def statistic1(self, s, studentList, listOfAverages):
        for i in studentList:
            if i.getStudentId() == s.getStudentId():
                listOfAverages.append(i)
        return listOfAverages

    def statistic2(self, discipline):
        bool = False
        for s in self.getEnrolledStudents(discipline.getDisciplineId()):
            studentList = self.__repoS.getAll()

            for i in studentList:
                if i.getStudentId() == s.getStudentId() and s.getValue() < 5:
                    bool = True
                    print(str(i.getStudentId()).ljust(10) + str(i.getName()).ljust(15)
                          + str(s.getValue()).ljust(10))

        if bool == False:
            print("Every student has passed at", discipline.getName())

    def statistic3(self, studentList, listOfAverages):
        for s in studentList:
            listOfGrades = self.getGrades(s.getStudentId())
            if len(listOfGrades) != 0:
                average = round(sum(listOfGrades) / len(listOfGrades))
                studentAverage = []
                studentAverage.append(s)
                studentAverage.append(average)
                listOfAverages.append(studentAverage)
        return listOfAverages

    def statistic4(self, disciplineList, listOfAverages):
        for d in disciplineList:
            listOfGrades = self.getGrades(d.getDisciplineId())
            if len(listOfGrades) != 0:
                average = int(sum(listOfGrades) / len(listOfGrades))
                school = []
                school.append(d)
                school.append(average)
                listOfAverages.append(school)
        return listOfAverages

