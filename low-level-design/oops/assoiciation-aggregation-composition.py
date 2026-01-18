from __future__ import annotations
from typing import List

# One to One Association
class Passport:
    __passportNumber: int

    def __init__(self, passportNumber: int):
        self.__passportNumber = passportNumber

    def getPassportNumber(self):
        return self.__passportNumber


class Person:
    __name: str
    __passport: Passport

    def __init__(self, name: str, passport: Passport):
        self.__name = name
        self.__passport = passport

    def displayDetails(self):
        print("Name : " + self.__name)
        print("Passport Number : " + str(self.__passport.getPassportNumber()))

# One to Many Association
class Student:
    __name: str
    __id: int

    def __init__(self, name: str, id: int):
        self.__name = name
        self.__id = id

    def displayDetails(self):
        print("Name : " + self.__name)
        print("ID : " + str(self.__id))

class College:
    __name: str
    __students: list[Student]

    def __init__(self, name: str):
        self.__name = name
        self.__students = []

    def addStudent(self, student: Student):
        self.__students.append(student)

    def displayDetails(self):
        print("Name : " + self.__name)
        for student in self.__students:
            student.displayDetails()

# Many to Many Association
class StudentCourse:
    __student: str
    __courses: List[Course]

    def __init__(self, student: str):
        self.__student = student
        self.__courses: List[Course] = []

    def addCourse(self, course: Course):
        self.__courses.append(course)

    def getName(self):
        return self.__student

    def displayDetails(self):
        print("Student : " + self.__student)
        for course in self.__courses:
            print("Course : " + course.getName())

class Course:
    __name: str
    __students: list[StudentCourse]

    def __init__(self, name: str):
        self.__name = name
        self.__students = []

    def addStudent(self, student: StudentCourse):
        self.__students.append(student)
    
    def getName(self):
        return self.__name

    def displayAllStudents(self):
        print("Course : " + self.__name)
        for student in self.__students:
            print("Student : " + student.getName())

# Aggregation -> Weak relationship and Person1 Doesn't Own Passport1
class Passport1:
    __passportNumber: int

    def __init__(self, passportNumber: int):
        self.__passportNumber = passportNumber

class Person1:
    __name: str
    __passport: Passport1

    def __init__(self, name: str, passport: Passport1):
        self.__name = name
        self.__passport = passport

# Composition -> Strong relationship and Person1 Owns Passport1
class Passport2:
    __passportNumber: int

    def __init__(self, passportNumber: int):
        self.__passportNumber = passportNumber    

class Person2:
    __name: str
    __passport: Passport2

    def __init__(self, name: str, passportNumber: int):
        self.__name = name
        self.__passport = Passport2(passportNumber)

if __name__ == "__main__":
    passport = Passport(1234567890)
    person = Person("John Doe", passport)
    person.displayDetails()

    student1 = Student("John Doe", 1)
    student2 = Student("Jane Doe", 2)
    college = College("ABC College")
    college.addStudent(student1)
    college.addStudent(student2)
    college.displayDetails()

    course1 = Course("Mathematics")
    course2 = Course("Computer Science")

    harry = StudentCourse("Harry Doe")
    hermione = StudentCourse("Hermione Doe")
    ron = StudentCourse("Ron Weasley")

    harry.addCourse(course1)
    harry.addCourse(course2)
    course1.addStudent(harry)
    course2.addStudent(harry)
    hermione.addCourse(course1)
    course1.addStudent(hermione)
    ron.addCourse(course2)
    course2.addStudent(ron)

    print("--------------------------------")
    course1.displayAllStudents()
    course2.displayAllStudents()

    print("--------------------------------")
    harry.displayDetails()
    hermione.displayDetails()
    ron.displayDetails()

    # Aggregation
    passport1 = Passport1(1234567890)
    person1 = Person1("John Doe", passport1)

    # Composition
    person2 = Person2("Jane Doe", 1234567890)





