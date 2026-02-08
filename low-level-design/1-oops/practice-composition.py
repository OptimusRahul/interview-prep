from __future__ import annotations
from typing import List

"""
Design a system to manage a composition relationship between a University and its Colleges. Implement the following:

University class :

Attribute: colleges (List of College objects), name (string)

Methods:

addCollege(collegeName, collegeId): Adds a college to the university.
displayDetails(): Prints the university's details along with all associated colleges.
College Class :

Attributes: name (String), id (String).



For output format refer the commented code on IDE.


Example 1

Input : name = "Global_University" ,

college Names = [ "COEP", "PICT", "VJTI", "WCE", "PCCOE" ]

college Id = [ "CO8543", "PI9514", "VJ8643", "VF569", "PC9246" ]

Output :

University Name : Global_University

College Name : COEP

College ID : CO8543

College Name : PICT

College ID : PI9514

College Name : VJTI

College ID : VJ8643

College Name : WCE

College ID : VF569

College Name : PCCOE

College ID : PC9246

Explanation :

First we create the object of class University with name as argument to constructor.
Then we call the method addCollege to add the mentioned college names and id under that university object.
Then the displayDetails method is called to display the content of the University and Colleges.
"""

class University:
    __name: str
    __colleges: List[College]

    def __init__(self, name: str):
        self.__name = name
        self.__colleges = []

    def addCollege(self, collegeName: str, collegeId: str):
        self.__colleges.append(College(collegeName, collegeId))

    def displayDetails(self):
        print("University Name : " + self.__name)
        for college in self.__colleges:
            college.displayDetails()

class College:
    __name: str
    __id: str

    def __init__(self, name: str, id: str):
        self.__name = name
        self.__id = id
    
    def displayDetails(self):
        print("College Name : " + self.__name)
        print("College ID : " + self.__id)


# This is the driver code that will execute and demonstrate the functionality of your class `University` and the class `College`.

def main():
    name = input()
    collegeName = input().split()
    collegeId = input().split()

    # Creating the object of class University with the name as constructor argument
    university = University(name)

    # Adding the college names and IDs using the addCollege method called through the university object
    for j in range(len(collegeName)):
        university.addCollege(collegeName[j], collegeId[j])

    # Calling the method displayDetails through the university object
    university.displayDetails()


if __name__ == "__main__":
    main()


"""
# Below is the output format

print("University Name : " + name)
print("College Name : " + name)
print("College ID : " + id)
"""
