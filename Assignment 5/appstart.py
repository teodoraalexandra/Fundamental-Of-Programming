from domain.student import Student
from operation.studentController import StudentController
from repository.studentRepo import StudentRepository
from repository.studentCSVFileRepository import StudentCSVFileRepository
from repository.studentPickleFileRepository import StudentPickleFileRepository

from domain.discipline import Discipline
from operation.disciplineController import DisciplineController
from repository.disciplineRepo import DisciplineRepository
from repository.disciplineCSVFileRepository import DisciplineCSVFileRepository
from repository.disciplinePickleFileRepository import DisciplinePickleFileRepository

from domain.grade import Grade
from operation.gradeController import GradeController
from repository.gradeRepo import GradeRepository
from repository.gradeCSVFileRepository import GradeCSVFileRepository
from repository.gradePickleFileRepository import GradePickleFileRepository

from operation.undoController import UndoController
from ui.menu import UI


def read_settings():
    f = open('settings.properties', 'r')
    s = f.read()
    lines = s.split('\n')

    settings = {}
    for line in lines:
        keyvalue = line.split('=')
        settings[keyvalue[0].strip()] = keyvalue[1].strip()

    return settings


def start():
    settings = read_settings()
    initialise = False
    if settings['repo_type'] == 'text':
        repoS = StudentCSVFileRepository()
        repoD = DisciplineCSVFileRepository()
        repoG = GradeCSVFileRepository()
    elif settings['repo_type'] == 'binary':
        repoS = StudentPickleFileRepository()
        repoD = DisciplinePickleFileRepository()
        repoG = GradePickleFileRepository()
    else:
        repoS = StudentRepository()
        repoS.initList()
        repoD = DisciplineRepository()
        repoD.initList()
        repoG = GradeRepository()
        repoG.initList()
        initialise = True

    undoController = UndoController()

    controllerS = StudentController(repoS, undoController)
    controllerD = DisciplineController(repoD)

    controllerG = GradeController(repoG, repoS, repoD)

    ui = UI(controllerS, controllerD, controllerG, undoController)

    ui.mainMenu()

start()