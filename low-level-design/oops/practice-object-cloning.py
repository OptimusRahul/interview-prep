"""
You are required to design a class hierarchy to demonstrate object cloning using shallow and deep copying in a library system. A Library contains a list of Book objects.

Shallow Copy: Creates a new object that shares references with the original object for nested structures.

Deep Copy: Creates a completely independent copy of the original object, including all nested structures.



Classes :

Book :

Attributes : title (string) , author (string)
Library :

Attributes : name (string) , books (List of Book class)
Methods :
shallowClone() : Creates a shallow copy of the Library object.
deepClone() : Creates a deep copy of Library object.
display() : Displays the output/ attributes of the class.
addBook (Book book) : It adds one book info to the list of books.


Refer the commented code on IDE to understand the output format using display method.

Refer the sample example output to understand the output format.


Example 1

Input : name = "Central_Library"

title = [ "Frankestein", "King_Arthur_and_the_Round_Table" ]

author = [ "Mary_Shelley", "Rosemary_Sutcliff" ]

changeIndex = 1

newTitle = "Treasure_Island"

new_author = "Robert_Louis_Stevenson"

Output :

Original Library :

Library : Central_Library

Book : Frankestein, Author : Mary_Shelley

Book : King_Arthur_and_the_Round_Table, Author : Rosemary_Sutcliff



After Modifications :



Original Library :

Library : Central_Library

Book : Frankestein, Author : Mary_Shelley

Book : Treasure_Island, Author : Robert_Louis_Stevenson



Shallow Clone :

Library : Central_Library

Book : Frankestein, Author : Mary_Shelley

Book : Treasure_Island, Author : Robert_Louis_Stevenson



Deep Clone :

Library : Central_Library

Book : Frankestein, Author : Mary_Shelley

Book : King_Arthur_and_the_Round_Table, Author : Rosemary_Sutcliff



Explanation :

First we will create a Library class object named 'library' with name being passed through constructor for initialization.
Then we will iterate over the title and author array to add them in the list of books present in the Library class.
Now a text is printed through driver code. And following it we call the display function of Library class to print the attributes of the library object that we set.
Next we will create the shallow clone object by calling the method shallowClone().
Next we will create the deep clone object by calling the method deepClone().
Now we will change the title and author of the index 'changeIndex' to newTitle and newAuthor for the original library object. (This will be done through driver code, you do not have to write this part).
Now we will print some text and call the display method through the original library object and print the attributes of Library class.
Next we will call the display method through shallow clone object and print the attributes of Library class.
Next we will call the display method through deep clone object and print the attributes of Library class.
As per output you can see, that the title and author for book at index = 1, have been changed in original library object and shallow clone object. But whereas the Deep clone object still has the old information.

This is what you should be able to achieve through your code.
"""

from typing import List, Optional
import copy

class Book:
    title: str
    author: str

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def clone(self):
        return Book(self.title, self.author)

class Library:
    name: str
    books: List[Book]

    def __init__(self, name: str, books: Optional[List[Book]] = None):
        self.name = name
        self.books = books if books is not None else []

    def addBook(self, book: Book):
        self.books.append(book)

    def shallowClone(self):
        return copy.copy(self)

    def deepClone(self):
        return Library(self.name, [book.clone() for book in self.books])

    def display(self):
        print("Library Name : " + self.name)
        for book in self.books:
            print("Book : " + book.title + ", Author : " + book.author)




def main():

    # Hardcoded example values
    name = "Central Library"
    titles = ["Book One", "Book Two", "Book Three"]
    authors = ["Author A", "Author B", "Author C"]

    # creating the Library class object
    library = Library(name)

    # adding the title and author names to in the list of books present in the class Library
    for j in range(len(titles)):
        library.addBook(Book(titles[j], authors[j]))

    print("Original Library : ")

    # calling the display function to display the original details that we set in above part of code
    library.display()

    # cloning objects using shallowClone and deepClone clone methods
    shallowLibrary = library.shallowClone()
    deepLibrary = library.deepClone()

    # Hardcoded which book and what to change
    changeIndex = 1
    changeTitle = "New Title"
    changeAuthor = "New Author"

    # changing the title and author of the book present at index changeIndex using the original library object
    library.books[changeIndex].title = changeTitle
    library.books[changeIndex].author = changeAuthor

    print("\nAfter Modification : ")
    print("\nOriginal Library : ")

    # calling the display method through original library object to print the output
    library.display()

    print("\nShallow Clone : ")

    # calling the display method through shallow clone object to print the output
    shallowLibrary.display()

    print("\nDeep Clone : ")

    # calling the display method through deep clone object to print the output
    deepLibrary.display()


if __name__ == "__main__":
    main()


"""
# Below are the output statements

print("Library : " + name)
print("Book : " + book.title + ", Author : " + book.author)
"""