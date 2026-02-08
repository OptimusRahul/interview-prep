"""
Design a class Employee to manage employee details securely using proper encapsulation and access modifiers. The class should implement the following attributes and methods :

Attributes :

name (string) : public, Represents the name of employee.
employeeId (Integer) : protected, Represents the unique Id of the employee.
salary (double) : private, Represents the salary of the employee.
Methods :

setSalary (double salary) : Sets the salary value, If salary is negative then print "Invalid salary" and set the salary to 0.
getSalary() : Return the salary value.
parameterised constructor to initialize the attributes. (If salary is negative then print "Invalid salary" and set the salary to 0.)
displayEmployeeDetails() : Display the employee details in format specified below :


Refer the sample examples for understanding the output format.

Refer the commented code to check the output statments.


Example 1

Input : name = "Striver" , employeeId = 9656 , salary = 10000 , newSalary = 15840

Output :

Salary : 10000.00

Name : Striver

Employee Id : 9656

Salary : 15840.00

Explanation :

An object employee of class Employee is created with parameterised constructor.
A call is given to the getSalary method and it is displayed through the driver program itself.
We call the setSalary method with newSalary as argument.
Then we call the displayEmployeeDetails() method to print the details of the employee.
Example 2

Input : name = "Striver" , employeeId = 9656 , salary = -1050, newSalary = -9315

Output :

Invalid salary

Salary : 0.00

Invalid salary

Name : Striver

Employee Id : 9656

Salary : 0.00

Explanation :

An object employee of class Employee is created with parameterised constructor. As the salary is in negative amount, so the constructor will print the text "Invalid salary" and set the salary to 0.00.
A call is given to the getSalary method and it is displayed through the driver program itself.
We call the setSalary method with newSalary as argument. As the newSalary is negative so we print the text "Invalid salary" and set the salary to 0.00.
Then we call the displayEmployeeDetails() method to print the details of the employee.
Constraints

1 <= salary, newSalary <= 106
"""

class Employee:
    name: str              # Public attribute
    _employeeId: int       # Protected attribute
    __salary: float        # Private attribute

    def __init__(self, name: str, employeeId: int, salary: float):
        self.name = name
        self._employeeId = employeeId
        if salary >= 0:
            self.__salary = salary
        else:
            self.__salary = 0.0
            print("Invalid salary")

    def getSalary(self):
        return self.__salary
    
    def setSalary(self, salary: float):
        if salary < 0:
            print("Invalid salary")
            self.__salary = 0.0
            return
        self.__salary = salary
    
    def displayEmployeeDetails(self):
        print("Name : " + self.name)
        print("Employee Id : " + str(self._employeeId))
        print("Salary : {:.2f}".format(self.__salary))

if __name__ == "__main__":

    name = "Striver"          # Name of the employee
    employeeId = 9656     # ID of the employee
    salary = 10000       # Initial salary
    newSalary = 15840    # Salary to be updated

    # Create an Employee object
    employee = Employee(name, employeeId, salary)

    # Get and print the salary
    print("Salary : {:.2f}".format(employee.getSalary()))

    # Update the salary
    employee.setSalary(newSalary)

    # Display employee details
    employee.displayEmployeeDetails()

'''
This is the driver code that will execute and demonstrate the functionality of your `Employee` class.

It creates an object of class `Employee`, the parameterized constructor sets the values of name, employeeId, and salary attributes.
It calls the getSalary method to display the salary set by the parameterized constructor.
It then calls the setSalary method to update the salary with newSalary.
Finally, displayEmployeeDetails is called to print the details of the employee in the specified format.


# Main function to demonstrate the functionality of the Employee class
if __name__ == "__main__":

    name = ""          # Name of the employee
    employeeId = 0     # ID of the employee
    salary = 0.0       # Initial salary
    newSalary = 0.0    # Salary to be updated

    # Create an Employee object
    employee = Employee(name, employeeId, salary)

    # Get and print the salary
    print("Salary : {:.2f}".format(employee.getSalary()))

    # Update the salary
    employee.setSalary(newSalary)

    # Display employee details
    employee.displayEmployeeDetails()
'''


'''
# Below is the output format

print("Name : " + name)
print("Employee Id : " + str(employeeId))
print("Salary : {:.2f}".format(salary))
'''
