"""
Design a system to manage the relationship between Employees and Departments using aggregation. Implement the following:

Department :

Attributes: name (String), id (String).

Method: displayDetails() - Prints the department details.

Employee :

Attributes: name (String), id (int), department (Department).

Method: displayDetails() - Prints the employee details, including the associated department details.


Refer the commented code for the output format.

Example 1

Input : E_name = "Striver" , D_name = "Management", E_id = 10434 , D_id = "MAN41241"

Output :

Employee Name : Striver

Employee Id : 10434

Department Name : Management

Department Id : MAN41241

Explanation :

First we create the object 'dep' of class Department with D_name, D_id as constructor parameters.
Then we create the object of class Employee with E_name, E_id, dep object as constructor parameters.
Next we call the display method through the Employee class object and print the details of both employee and department class attributes.
"""

class Department:
    __name: str
    __id: str

    def __init__(self, name: str, id: str):
        self.__name = name
        self.__id = id

    def displayDetails(self):
        print("Department Name : " + self.__name)
        print("Department Id : " + self.__id)

class Employee:
    __name: str
    __id: int
    __department: Department
        
    def __init__(self, name: str, id: int, department: Department):
        self.__name = name
        self.__id = id
        self.__department = department

    def displayDetails(self):
        print("Employee Name : " + self.__name)
        print("Employee Id : " + str(self.__id))
        self.__department.displayDetails()

def main():
    # Taking input
    E_name = input()  # Employee name
    D_name = input()  # Department name
    E_id = int(input())  # Employee ID
    D_id = input()  # Department ID

    # creates an object of Department class with D_name, D_id as the arguments
    department = Department(D_name, D_id)

    # creates an object of Employee class with E_name, E_id, department as the arguments
    employee = Employee(E_name, E_id, department)

    # calls the display method using the employee object
    employee.displayDetails()


if __name__ == "__main__":
    main()

'''
# Below is the output format

print("Employee Name : " + name)
print("Employee Id : " + id)
print("Department Name : " + name)
print("Department Id : " + id)
''' 