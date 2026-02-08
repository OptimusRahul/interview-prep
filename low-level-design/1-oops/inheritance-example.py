# Parent class or super class
class School:
    # Private attribute for school name
    __schoolName: str

    # Constructor initializes the school name
    def __init__(self):
        self.__schoolName = "DPS"  # Default school name

    # Method to print the school name
    def printSchoolName(self):
        print("School name: " + self.__schoolName)


# Subclass or child class
class Student(School):
    # Private attribute for student name
    __studentName: str

    # Constructor initializes the student name
    def __init__(self, name: str):
        super().__init__()  # MUST explicitly call parent constructor in Python
        self.__studentName = name

    # Method to print the student name
    def printStudentName(self):
        print("Student name: " + self.__studentName)


# Main execution
if __name__ == "__main__":
    # Create a new student object with the name "Raj"
    student = Student("Raj")

    # Print the student's name
    student.printStudentName()

    # Print the school's name
    student.printSchoolName()
