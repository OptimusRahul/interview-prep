class School:
    __schoolName: str
    __principal: str

    def __init__(self, schoolName: str = "St. John's School"):
        self.__schoolName = schoolName
        self.__principal = "Mrs. Johnson"
    
    def getSchoolName(self):
        print("School Name : " + self.__schoolName)

    def getPrincipal(self):
        print("Principal : " + self.__principal)

class Student(School):
    __studentName: str

    def __init__(self, studentName: str = "John Doe"):
        super().__init__()
        self.__studentName = studentName
    
    def getStudentName(self):
        print("Student Name : " + self.__studentName)

    def getSchoolName(self):
        print("School Name : " + self.__studentName)

class Teacher(School):
    __teacherName: str
    __subject: str

    def __init__(self, teacherName: str = "Jane Doe", subject: str = "Mathematics"):
        super().__init__()
        self.__teacherName = teacherName
        self.__subject = subject
    
    def getTeacherName(self):
        print("Teacher Name : " + self.__teacherName)
        print("Subject : " + self.__subject)

class Parent(Student):
    __parentName: str

    def __init__(self, parentName: str = "John Doe"):
        super().__init__()
        self.__parentName = parentName
    
    def getParentName(self):
        print("Parent Name : " + self.__parentName)



class Main():
    def main(self):

        # Single inheritance
        # school = School()
        # student = Student("Jane Doe")
        # student.getSchoolName()
        # student.getStudentName()

        # Multi-level inheritance
        # parent = Parent("Laura Doe")
        # parent.getParentName()
        # parent.getStudentName()
        # parent.getSchoolName()

        # Multiple inheritance
        teacher = Teacher("Mr. Smith", "Mathematics")
        teacher.getTeacherName()
        teacher.getSchoolName()


        # Hierarchical inheritance
        student = Student("Jane Doe")
        student.getStudentName()
        student.getSchoolName()


if __name__ == "__main__":
    main = Main()
    main.main()