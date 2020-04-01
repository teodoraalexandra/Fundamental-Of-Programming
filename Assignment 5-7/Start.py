
from Library import *

studentDB = StudentDataBase()
'''
studentDB.add(Student(1, "Jake Walker"))
studentDB.add(Student(24, "Nicholas White"))
studentDB.add(Student(55, "Joe Wood"))
studentDB.add(Student(16, "George Austin"))
studentDB.add(Student(19, "John Robertson"))
studentDB.add(Student(20, "Simon Ortega"))
studentDB.add(Student(75, "Vincent Armstrong"))
studentDB.add(Student(66, "Gilbert Avila"))
studentDB.add(Student(32, "Johann Thomas"))
studentDB.add(Student(77, "Yael Mcclain"))
'''
studentDB.initList()
disciplineDB = DisciplineDataBase()

disciplineDB.add(Discipline(1, "Mathematics"))
disciplineDB.add(Discipline(12, "Computer Science"))
disciplineDB.add(Discipline(31, "French"))
disciplineDB.add(Discipline(44, "English"))
disciplineDB.add(Discipline(56, "Physics"))
disciplineDB.add(Discipline(92, "Geography"))
disciplineDB.add(Discipline(63, "Biology"))
disciplineDB.add(Discipline(55, "History"))
disciplineDB.add(Discipline(10, "Physical Education"))
disciplineDB.add(Discipline(4, "Music"))

gradeDB = GradeDataBase()
'''
gradeDB.add(Grade(55, 77, 9))
gradeDB.add(Grade(10,24,6))
gradeDB.add(Grade(63,16,7))
gradeDB.add(Grade(63,19,10))
gradeDB.add(Grade(44,77,2))
gradeDB.add(Grade(31,20,3))
gradeDB.add(Grade(4,75,6))
gradeDB.add(Grade(12,66,1))
gradeDB.add(Grade(55,32,9))
gradeDB.add(Grade(92,24,10))
'''
gradeDB.initList(studentDB,disciplineDB)

gradeController = GradeController(gradeDB)

studentController = StudentController(studentDB)

disciplineController = DisciplineController(disciplineDB)

ui = UI(studentController, disciplineController, gradeController)

ui.selectOption()
