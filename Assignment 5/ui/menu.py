from domain.student import Student
from domain.discipline import Discipline
from domain.grade import Grade
from operation.undoController import *
import re
from operator import itemgetter
from operation.sortModule import *
from operation.filterModule import *

class UI:
    def __init__(self, controllerS, controllerD, controllerG, undoController):
        self._controllerS = controllerS
        self._controllerD = controllerD
        self._controllerG = controllerG
        self._undoController = undoController

    def mainMenu(self):
        ok = True
        while ok:
            try:
                UI.printMenu(self)
                command = input("Enter command: ")
                if command == '0':
                    print("Bye bye")
                    ok = False

                elif command == "1":
                    print("\n1. Add student")
                    print("2. Remove student")
                    print("3. Update student")
                    print("4. Display students")
                    print('5. Display grades for a student')

                    option = input("Enter your option: ")

                    if option == '1':
                        s = UI.readStudent(self)
                        if self._controllerS.checkId(s):
                            raise ValueError("This ID already exist. Try again!")
                        else:
                            self._controllerS.addStudent(s)
                            undoOperation = FunctionCall(self._controllerS.removeStudent, s)
                            redoOperation = FunctionCall(self._controllerS.addStudent, s)

                            operation = Operation(undoOperation, redoOperation)
                            self._undoController.addOperation(operation)

                    elif option == '2':
                        s = UI.readStudent(self)
                        self._controllerS.removeStudent(s)

                        undoOperation = FunctionCall(self._controllerS.addStudent, s)
                        redoOperation = FunctionCall(self._controllerS.removeStudent, s)
                        cascadeRemove = CascadeOperation()
                        operation = Operation(undoOperation, redoOperation)
                        cascadeRemove.add(operation)

                        listOfGrades = self._controllerG.getStudentGrades(s.getStudentId())
                        for grade in listOfGrades:
                            self._controllerG.removeGrade(grade)
                            undoOperation = FunctionCall(self._controllerG.addGrade, grade)
                            redoOperation = FunctionCall(self._controllerG.removeGrade, grade)
                            operation = Operation(undoOperation, redoOperation)
                            cascadeRemove.add(operation)

                        self._undoController.addOperation(cascadeRemove)

                    elif option == '3':
                        print('Enter the student you want to update: ')
                        o = UI.readStudent(self)
                        print('Enter the new student you want to update with: ')
                        n = UI.readStudent(self)

                        undoOperation = FunctionCall(self._controllerS.updateStudent, n, o)
                        redoOperation = FunctionCall(self._controllerS.updateStudent, o, n)
                        operation = Operation(undoOperation, redoOperation)
                        self._undoController.addOperation(operation)

                        self._controllerS.updateStudent(o, n)


                    elif option == '4':
                        for s in self._controllerS.getAll():
                            print(str(s))

                    elif option == '5':
                        s = UI.readStudent(self)
                        if s in self._controllerS.getAll():
                            listOfGrades = self._controllerG.getStudentGrades(s.getStudentId())
                            listOfDisciplines = self._controllerD.getAll()

                            print('The grades are: ')
                            for i in listOfGrades:
                                print(str(int(i.getValue())) + " at ", end="")
                                for j in listOfDisciplines:
                                    if i.getDisciplineId() == j.getDisciplineId():
                                        print(j.getName())
                        else:
                            raise ValueError("The student was not found.")

                    else:
                        raise ValueError("Invalid command")

                elif command == '2':
                    print("\n1. Add discipline")
                    print("2. Remove discipline")
                    print("3. Update discipline")
                    print("4. Display disciplines")
                    print('5. Display students enrolled to a discipline')
                    option = input("Enter your option: ")

                    if option == "1":
                        d = UI.readDiscipline(self)
                        if self._controllerD.checkId(d):
                            raise ValueError("This ID already exist. Try again!")
                        else:
                            self._controllerD.addDiscipline(d)
                            undoOperation = FunctionCall(self._controllerD.removeDiscipline, d)
                            redoOperation = FunctionCall(self._controllerD.addDiscipline, d)

                            operation = Operation(undoOperation, redoOperation)
                            self._undoController.addOperation(operation)

                    elif option == "2":
                        d = UI.readDiscipline(self)
                        self._controllerD.removeDiscipline(d)

                        undoOperation = FunctionCall(self._controllerD.addDiscipline, d)
                        redoOperation = FunctionCall(self._controllerD.removeDiscipline, d)
                        cascadeRemove = CascadeOperation()
                        operation = Operation(undoOperation, redoOperation)
                        cascadeRemove.add(operation)

                        listOfStudents = self._controllerG.getEnrolledStudents(d.getDisciplineId())
                        for grade in listOfStudents:
                            self._controllerG.removeGrade(grade)
                            undoOperation = FunctionCall(self._controllerG.addGrade, grade)
                            redoOperation = FunctionCall(self._controllerG.removeGrade, grade)
                            operation = Operation(undoOperation, redoOperation)
                            cascadeRemove.add(operation)

                        self._undoController.addOperation(cascadeRemove)

                    elif option == "3":
                        print('Enter the discipline you want to update: ')
                        o = UI.readDiscipline(self)
                        print('Enter the new discipline you want to update with: ')
                        n = UI.readDiscipline(self)

                        undoOperation = FunctionCall(self._controllerD.updateDiscipline, n, o)
                        redoOperation = FunctionCall(self._controllerD.updateDiscipline, o, n)
                        operation = Operation(undoOperation, redoOperation)
                        self._undoController.addOperation(operation)

                        self._controllerD.updateDiscipline(o, n)

                    elif option == "4":
                        for d in self._controllerD.getAll():
                            print(str(d))

                    elif option == "5":
                        d = UI.readDiscipline(self)
                        if d in self._controllerD.getAll():
                            listOfEnrolled = self._controllerG.getEnrolledStudents(d.getDisciplineId())
                            listOfStudents = self._controllerS.getAll()

                            print('The students enrolled in the course ' + d.getName() + " are: ")
                            for s in listOfEnrolled:
                                print(str(s.getStudentId()) + " ", end="")
                                for j in listOfStudents:
                                    if s.getStudentId() == j.getStudentId():
                                        print(j.getName())
                        else:
                            raise ValueError("The discipline was not found.")

                    else:
                        raise ValueError('Invalid command')

                elif command == '3':
                    g = UI.readGrade(self)
                    self._controllerG.addGrade(g)

                    undoOperation = FunctionCall(self._controllerG.removeGrade, g)
                    redoOperation = FunctionCall(self._controllerG.addGrade, g)

                    operation = Operation(undoOperation, redoOperation)
                    self._undoController.addOperation(operation)

                elif command == '4':
                    option = input("Do you want to search for disciplines or students? Type d or s: ")
                    if option == 'd':
                        print("Enter the name of discipline you want to search: ")
                        discipline = UI.readDiscipline(self)
                        disciplineList = self._controllerD.getAll()

                        nameList = []
                        for i in disciplineList:
                            nameList.append(i.getName())

                        print(filter(nameList, discipline.getName(), partString))

                    elif option == 's':
                        print("Enter the name of student you want to search: ")
                        student = UI.readStudent(self)
                        studentList = self._controllerS.getAll()

                        nameList = []
                        for i in studentList:
                            nameList.append(i.getName())

                        print(filter(nameList, student.getName(), partString))

                    else:
                        raise ValueError("You have to type d or s")

                elif command == '5':
                    print('There are 4 statistics: ')
                    print('1. All students enrolled at a given discipline.')
                    print('2. All students failing at a given discipline.')
                    print('3. Students with the best school situation.')
                    print('4. All disciplines at which there is at least one grade.')

                    option = input('Which statistic do you want to see? ')
                    if option == '1':
                        print("All students enrolled at a given discipline: ")
                        discipline = UI.readDiscipline(self)
                        listOfAverages = []

                        print("-" * 70)

                        print("Discipline is: ", discipline.getName())
                        print("ID".ljust(10) + "Name".ljust(15))

                        for s in self._controllerG.getEnrolledStudents(discipline.getDisciplineId()):
                            studentList = self._controllerS.getAll()
                            listOfAverages = self._controllerG.statistic1(s, studentList, listOfAverages)

                        sortList = gnomeSort(listOfAverages, key_name)

                        for i in sortList:
                            print(str(i.getStudentId()).ljust(10) + str(i.getName()).ljust(15))

                        print("-" * 70)

                    elif option == '2':
                        print("All students failed at a given discipline: ")
                        discipline = UI.readDiscipline(self)
                        listOfFailed = []

                        print("-" * 70)

                        print("Discipline is: ", discipline.getName())
                        print("ID".ljust(10) + "Name".ljust(15) + "Grade".ljust(10))

                        listOfFailed = self._controllerG.statistic2(discipline)

                        print("-" * 70)

                    elif option == '3':
                        print("All students with the best school situation: ")
                        studentList = self._controllerS.getAll()
                        listOfAverages = []

                        print("-" * 70)

                        print("ID".ljust(10) + "Name".ljust(15) + "Average grade".ljust(10))

                        listOfAverages = self._controllerG.statistic3(studentList, listOfAverages)

                        sortList = gnomeSort(listOfAverages, key_name_average)
                        sortList.reverse()
                        sortList = gnomeSort(listOfAverages, key_average)
                        sortList.reverse()

                        for i in sortList:
                            print(str(i[0].getStudentId()).ljust(10) + str(i[0].getName()).ljust(15) + str(i[1]))

                        print("-" * 70)

                    elif option == '4':
                        print("All disciplines at which there is at least one grade: ")
                        disciplineList = self._controllerD.getAll()
                        listOfAverages = []

                        print("-" * 70)

                        print("ID".ljust(10) + "Discipline".ljust(15) + "Average grade".ljust(10))

                        listOfAverages = self._controllerG.statistic4(disciplineList, listOfAverages)

                        sortList = gnomeSort(listOfAverages, key_average)
                        sortList.reverse()

                        for i in sortList:
                            print(str(i[0].getDisciplineId()).ljust(10) + str(i[0].getName()).ljust(15) + str(i[1]))

                        print("-" * 70)

                    else:
                        raise ValueError('We have only 4 statistics.')

                elif command == '6':
                    self._undoController.undo()

                elif command == '7':
                    self._undoController.redo()

                else:
                    raise ValueError("Invalid command. Enter 1, 2, 3, 4, 5 or 0")

            except Exception as me:
                print(me)


    def readStudent(self):
        while True:
            try:
                studentId = int(input("Enter student ID= "))
                name = str(input("Enter student name= "))
                return Student(studentId, name)
            except ValueError:
                print("Either ID or name are invalid!")
        return []

    def readDiscipline(self):
        while True:
            try:
                disciplineId = int(input("Enter discipline ID= "))
                name = str(input("Enter discipline name= "))
                return Discipline(disciplineId, name)
            except ValueError:
                print("Either ID or name are invalid!")
        return []

    def readGrade(self):
        print("Student info: ")
        student = UI.readStudent(self)
        print("Discipline info: ")
        discipline = UI.readDiscipline(self)
        gradeValue = input("Grade value: ")
        try:
            gradeValue = float(gradeValue)
        except Exception:
            raise ValueError("The grade must be a number")
        return Grade(discipline.getDisciplineId(), student.getStudentId(), gradeValue)

    def printMenu(self):
        menu = "\nCommands:\n"
        menu += "\t1. Operations for students\n"
        menu += "\t2. Operations for disciplines\n"
        menu += "\t3. Grade a student\n"
        menu += "\t4. Search for disciplines or students\n"
        menu += "\t5. Print the statistics\n"
        menu += "\t6. Undo\n"
        menu += "\t7. Redo\n"
        menu += "\t0. Exit\n"
        print(menu)
