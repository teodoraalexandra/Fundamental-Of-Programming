import unittest

from domain.student import Student
from repository.studentRepo import StudentRepository

from domain.discipline import Discipline
from repository.disciplineRepo import DisciplineRepository

from domain.grade import Grade
from repository.gradeRepo import GradeRepository

from operation.sortModule import *
from operation.filterModule import *

class moduleTest(unittest.TestCase):
    def test_student(self):
        self.assertEqual(str(Student(1, 'Teodora')), '1 Teodora')
        self.assertEqual(str(Student(2, 'Alexandra')), '2 Alexandra')
        self.assertEqual(str(Student(3, 'Iulia')), '3 Iulia')
        self.assertEqual(str(Student(4, 'Liviu')), '4 Liviu')
        self.assertEqual(str(Student(5, 'Rares')), '5 Rares')
        self.assertEqual(str(Student(6, 'Marcel')), '6 Marcel')
        self.assertEqual(str(Student(7, 'Doru')), '7 Doru')
        self.assertEqual(str(Student(8, 'Ovidiu')), '8 Ovidiu')

        self.assertEqual(str(Student(9, 'Radu')), str(Student(9, 'Radu')))
        self.assertFalse((Student(10, 'Bianca') == Student(9, 'Teodora')))

    def test_discipline(self):
        self.assertEqual(str(Discipline(1, 'Analiza')), '1 Analiza')
        self.assertEqual(str(Discipline(2, 'Algebra')), '2 Algebra')
        self.assertEqual(str(Discipline(3, 'Logica')), '3 Logica')
        self.assertEqual(str(Discipline(4, 'Geometrie')), '4 Geometrie')
        self.assertEqual(str(Discipline(5, 'ASC')), '5 ASC')
        self.assertEqual(str(Discipline(6, 'Programare')), '6 Programare')
        self.assertEqual(str(Discipline(7, 'OOP')), '7 OOP')
        self.assertEqual(str(Discipline(8, 'Comunicare')), '8 Comunicare')

        self.assertEqual(str(Discipline(9, 'Psihologie')), str(Discipline(9, 'Psihologie')))
        self.assertFalse((Discipline(10, 'Sport') == Discipline(11, 'Istorie')))

    def test_grade(self):
        self.assertEqual(str(Grade(101, 1, 10)), '101 1 10')
        self.assertEqual(str(Grade(234, 2, 4)), '234 2 4')
        self.assertEqual(str(Grade(324, 3, 7)), '324 3 7')
        self.assertEqual(str(Grade(467, 4, 5)), '467 4 5')
        self.assertEqual(str(Grade(587, 8, 8)), '587 8 8')
        self.assertEqual(str(Grade(698, 9, 9)), '698 9 9')
        self.assertEqual(str(Grade(704, 12, 4)), '704 12 4')
        self.assertEqual(str(Grade(845, 34, 3)), '845 34 3')

        self.assertEqual(str(Grade(102, 36, 2)), str(Grade(102, 36, 2)))
        self.assertFalse((Grade(923, 4, 5) == Grade(234, 4, 6)))

    def test_student_add(self):
        repoS = StudentRepository()
        testList = [Student(1, 'Teodora'), Student(2, 'Alexandra'), Student(3, 'Dan')]
        for i in range(0, len(testList)):
            repoS.add(testList[i])
            self.assertEqual(repoS.get(i), testList[i])

    def test_student_update(self):
        repoS = StudentRepository()
        oldStudent = Student(1, 'Teodora')
        newStudent = Student(11, 'Bianca')

        for i in range(0, len(repoS)):
            repoS.update(oldStudent, newStudent)
            self.assertEqual(repoS.get(i), newStudent)

    def test_student_remove(self):
        repoS = StudentRepository()
        repoS.add(Student(1, 'Teodora'))
        repoS.add(Student(2, 'Alexandra'))
        repoS.add(Student(3, 'Dan'))
        repoS.add(Student(4, 'Ovidiu'))
        repoS.add(Student(5, 'Radu'))
        repoS.add(Student(6, 'Ionut'))
        repoS.add(Student(7, 'Bianca'))
        repoS.add(Student(8, 'Malina'))
        repoS.add(Student(9, 'Dan'))
        repoS.add(Student(10, 'Ilinca'))
        initial = len(repoS)

        repoS.remove(Student(1, 'Teodora'))
        self.assertEqual(len(repoS), int(initial - 1))

        repoS.remove(Student(5, 'Radu'))
        self.assertEqual(len(repoS), int(initial - 2))

        repoS.remove(Student(8, 'Malina'))
        self.assertEqual(len(repoS), int(initial - 3))

    def test_discipline_add(self):
        repoD = DisciplineRepository()
        testList = [Discipline(111, 'Logica'), Discipline(222, 'Analiza'), Discipline(333, 'Algebra')]
        for i in range(0, len(testList)):
            repoD.add(testList[i])
            self.assertEqual(repoD.get(i), testList[i])

    def test_student_update(self):
        repoD = DisciplineRepository()
        oldDiscipline = Discipline(111, 'Logica')
        newDiscipline = Discipline(200, 'Istorie')

        for i in range(0, len(repoD)):
            repoD.update(oldDiscipline, newDiscipline)
            self.assertEqual(repoD.get(i), newDiscipline)

    def test_discipline_remove(self):
        repoD = DisciplineRepository()
        repoD.add(Discipline(111, 'Logica'))
        repoD.add(Discipline(222, 'Analiza'))
        repoD.add(Discipline(333, 'Algebra'))
        repoD.add(Discipline(444, 'Programare'))
        repoD.add(Discipline(555, 'ASC'))
        repoD.add(Discipline(666, 'Sport'))
        repoD.add(Discipline(777, 'Psihologie'))
        repoD.add(Discipline(888, 'Comunicare'))
        repoD.add(Discipline(999, 'Geometrie'))
        repoD.add(Discipline(100, 'Grafuri'))
        initial = len(repoD)

        repoD.remove(Discipline(222, 'Analiza'))
        self.assertEqual(len(repoD), int(initial - 1))

        repoD.remove(Discipline(666, 'Sport'))
        self.assertEqual(len(repoD), int(initial - 2))

        repoD.remove(Discipline(100, 'Grafuri'))
        self.assertEqual(len(repoD), int(initial - 3))

    def test_grade_add(self):
        repoG = GradeRepository()
        testList = [Grade(111, 1, 7), Grade(222, 2, 7), Grade(333, 3, 4)]
        for i in range(0, len(testList)):
            repoG.add(testList[i])
            self.assertEqual(repoG.get(i), testList[i])

    def test_grade_remove(self):
        repoG = GradeRepository()
        repoG.add(Grade(111, 1, 7))
        repoG.add(Grade(333, 2, 5))
        repoG.add(Grade(999, 3, 2))
        repoG.add(Grade(666, 4, 5))
        repoG.add(Grade(555, 5, 6))
        repoG.add(Grade(444, 6, 6))
        repoG.add(Grade(555, 7, 6))
        repoG.add(Grade(333, 8, 2))
        initial = len(repoG)

        repoG.remove(Grade(333, 2, 5))
        self.assertEqual(len(repoG), int(initial - 1))

        repoG.remove(Grade(444, 6, 6))
        self.assertEqual(len(repoG), int(initial - 2))

        repoG.remove(Grade(333, 8, 2))
        self.assertEqual(len(repoG), int(initial - 3))

    def test_sort(self):
        listToBeSorted = [Student(1, 'Teodora'), Student(6, 'Bianca'), Student(3, 'Denisa'), Student(2, 'Ioana')]
        gnomeSort(listToBeSorted, key_ids)
        self.assertEqual(listToBeSorted, [Student(1, 'Teodora'), Student(2, 'Ioana'), Student(3, 'Denisa'), Student(6, 'Bianca')])

        gnomeSort(listToBeSorted, key_name)
        self.assertEqual(listToBeSorted, [Student(6, 'Bianca'), Student(3, 'Denisa'), Student(2, 'Ioana'), Student(1, 'Teodora')])

    def test_filter(self):
        varste = [5, 12, 17, 18, 24, 32]
        numere = [3, 5, -5, 0, -6, -7, 8]

        list1 = filter(varste, 18, greater)
        list2 = filter(numere, 0, greater)

        self.assertEqual(list1, [5, 12, 17])
        self.assertEqual(list2, [-5, -6, -7])





