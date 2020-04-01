class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

class Student(Person):
    def __init__(self, name, faculty):
        Person.__init__(self, name)
        self._faculty = faculty

    @property
    def faculty(self):
        return self._faculty

p1 = Person('Alice')
s1 = Student('Bob', 'Math and CS')

print(str(s1))
print(p1.name)
print(s1.name)

print(s1.faculty)

print(isinstance(p1, Person))
print(isinstance(p1, Student))
print(isinstance(s1, Person))
print(isinstance(s1, Student))