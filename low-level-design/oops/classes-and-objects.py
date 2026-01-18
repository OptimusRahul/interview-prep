class Student:
    name: str
    rollNumber: int

    def setDetails(self, name, rollNumber):
        self.name = name
        self.rollNumber = rollNumber
    
    def displayDetails(self):
        print("Name : " + self.name)
        print("Roll Number : " + str(self.rollNumber))

if __name__ == "__main__":

    # Create an input prompt for taking input from the user
    name = input()  # Read the name as a string input

    rollNumber = int(input())  # Read the roll number as an integer input

    # Create an object of the Student class
    student = Student()

    # Set the details of the student using the setDetails() method
    student.setDetails(name, rollNumber)

    # Display the student's details using the displayDetails() method
    student.displayDetails()