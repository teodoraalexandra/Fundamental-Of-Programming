from domain.Student import Student
from domain.Discipline import Discipline
from domain.Grade import Grade


class UI:
    def __init__(self, studentController, disciplineController, gradeController):
        self._studentController = studentController
        self._disciplineController = disciplineController
        self._gradeController = gradeController

    def selectOption(self):
        while True:
            try:
                UI.printMenu(self)
                option = input("Enter option: ")
                if option == '0':
                    return False
                if option == '1':
                    print("\n1. Add Student")
                    print("2. Remove Student")
                    print("3. Update Student")
                    print("4. Display Students")
                    print("5. Display Grades for a student")
                    command = input("Enter option: ")
                    if command == '1':
                        student = UI.readStudent(self)
                        self._studentController.addStudent(student)
                        print("Operation successful!")
                    elif command == '2':
                        student = UI.readStudent(self)
                        self._studentController.removeStudent(student)
                        listOfGrades = self._gradeController.getStudentGrades(student.getID())
                        for grade in listOfGrades:
                            self._gradeController.removeGrade(grade)
                        print("Operation successful!")
                    elif command == '3':
                        print("Enter the student you want to update:\n")
                        oldStudent = UI.readStudent(self)
                        print("Please enter the updated student")
                        newStudent = UI.readStudent(self)
                        self._studentController.updateStudent(oldStudent, newStudent)
                        print("Operation successful!")
                    elif command == '4':
                        print("%-10s" % "ID" + "%16s" % "Name")
                        print(str(self._studentController))
                    elif command == '5':
                        student = UI.readStudent(self)
                        listOfGrades = self._gradeController.getStudentGrades(student.getID())
                        print("The grades are: ")
                        for i in listOfGrades:
                            print(str(i.getGrade()) + " at " + (str(i.getDiscID()) + " - " + str(self._disciplineController.findByID(i.getDiscID()))))
                    else:
                        raise ValueError("Error: Invalid command!")
                elif option == '2':
                    print("\n1. Add Discipline")
                    print("2. Remove Discipline")
                    print("3. Update Discipline")
                    print("4. Display Disciplines")
                    print("5. Display students enrolled to a discipline")
                    command = input("Enter option: ")
                    if command == '1':
                        discipline = UI.readDiscipline(self)
                        self._disciplineController.addDiscipline(discipline)
                        print("Operation successful!")
                    elif command == '2':
                        discipline = UI.readDiscipline(self)
                        self._disciplineController.removeDiscipline(discipline)
                        listOfStudents = self._gradeController.getEnrolledStudents(discipline.getID())
                        for grade in listOfStudents:
                            self._gradeController.removeGrade(grade)
                        print("Operation successful!")
                    elif command == '3':
                        print("Enter the discipline you want to update:")
                        oldDiscipline = UI.readDiscipline(self)
                        print("Please enter the updated discipline:")
                        newDiscipline = UI.readStudent(self)
                        self._disciplineController.updateDiscipline(oldDiscipline, newDiscipline)
                        print("Operation successful!")
                    elif command == '4':
                        print("%-10s" % "ID" + "%16s" % "Discipline Name")
                        print(str(self._disciplineController))
                    elif command == '5':
                        discipline = UI.readDiscipline(self)
                        listOfStudents = self._gradeController.getEnrolledStudents(discipline.getID())
                        print("The students enrolled in the course " + discipline.getName() + " are:")
                        print("ID   Name")
                        for student in listOfStudents:
                            print(str(student.getStudID()) + "   " + str(self._studentController.findByID(student.getStudID())))
                    else:
                        raise ValueError("Error: Invalid command!")
                elif option == '3':
                        print("\n1. Grade student at a given discipline")
                        #print("2. Display grades for a student")
                        command = input("Please input the option: ")
                        if command == '1':
                            grade = UI.readGrade(self)
                            self._gradeController.addGrade(grade)
                            print('Operation successful!')
                        else:
                            raise ValueError("Error: Invalid Command")
                else:
                    raise ValueError("Error: Invalid option!")
            except Exception as me:
                print(me)

    def readStudent(self):
        studentID = input("Please enter the ID: ")
        studentName = input("Please enter the name: ")
        return Student(studentID, studentName)

    def readDiscipline(self):
        disciplineID = input("Please enter the ID: ")
        disciplineName = input("Please enter the name: ")
        return Discipline(disciplineID,disciplineName)

    def readGrade(self):
        print("Student info:")
        student = UI.readStudent(self)
        print("Discipline info:")
        discipline = UI.readDiscipline(self)
        gradeValue = input("Grade value: ")
        try:
            gradeValue = float(gradeValue)
        except Exception:
            raise ValueError("The grade needs to be a number!")
        return Grade(discipline.getID(), student.getID(), gradeValue)

    def printMenu(self):
        menu = "\nCommands:\n"
        menu += "\t1. Student Operations\n"
        menu += "\t2. Discipline Operations\n"
        menu += "\t3. Grade Operations\n"
        menu += "\t0. Exit\n"
        print(menu)
