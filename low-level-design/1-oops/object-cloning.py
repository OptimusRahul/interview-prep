from typing import List
import copy

# Shallow Copy
# class Passport:
#     passportNumber: str

#     def __init__(self, passportNumber: str):
#         self.passportNumber = passportNumber

#     def __str__(self):
#         return self.passportNumber

# class Student:
#     name: str
#     passport: Passport

#     def __init__(self, name: str, passport: Passport):
#         self.name = name
#         self.passport = passport

#     def clone(self):
#         return copy.copy(self)

class Passport:
    passportNumber: str

    def __init__(self, passportNumber: str):
        self.passportNumber = passportNumber

    def __str__(self):
        return self.passportNumber

    def clone(self):
        return Passport(self.passportNumber)

class Student:
    name: str
    passport: Passport

    def __init__(self, name: str, passport: Passport):
        self.name = name
        self.passport = passport

    def clone(self):
        return Student(self.name, self.passport.clone())

if __name__ == "__main__":
    passport = Passport("1234567890")
    student = Student("John Doe", passport)

    student2 = student.clone()
    student2.name = "Jane Doe"
    student2.passport.passportNumber = "0987654321"

    print("Student 1:")
    print(student.name)
    print(student.passport)
    print("Student 2:")
    print(student2.name)
    print(student2.passport)