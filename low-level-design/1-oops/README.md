# Object-Oriented Programming (OOP) in Python

A comprehensive knowledge base covering all fundamental and advanced Object-Oriented Programming concepts with Python implementations. This collection contains 30+ practical examples demonstrating OOP principles, patterns, and best practices.

## Table of Contents

- [Introduction to OOP](#introduction-to-oop)
- [Core Concepts](#core-concepts)
- [The Four Pillars of OOP](#the-four-pillars-of-oop)
- [Advanced Concepts](#advanced-concepts)
- [Object Relationships](#object-relationships)
- [Additional Features](#additional-features)
- [File Index](#file-index)
- [Learning Roadmap](#learning-roadmap)

## Introduction to OOP

Object-Oriented Programming is a programming paradigm based on the concept of "objects" which contain data (attributes) and code (methods). OOP focuses on organizing software design around data, or objects, rather than functions and logic.

### Why OOP?

- **Modularity**: Code is organized into self-contained objects
- **Reusability**: Objects can be reused across programs
- **Flexibility**: Easy to modify and extend
- **Maintainability**: Changes in one part don't affect others
- **Security**: Data hiding through encapsulation

## Core Concepts

### 1. Classes and Objects

**File:** `classes-and-objects.py`

A **class** is a blueprint for creating objects. An **object** is an instance of a class.

```python
class Student:
    name: str
    rollNumber: int

    def setDetails(self, name, rollNumber):
        self.name = name
        self.rollNumber = rollNumber
    
    def displayDetails(self):
        print("Name : " + self.name)
        print("Roll Number : " + str(self.rollNumber))

# Creating an object
student = Student()
student.setDetails("John Doe", 101)
student.displayDetails()
```

**Key Points:**
- Classes define the structure and behavior
- Objects are instances with actual data
- Methods define what objects can do

**Related Files:**
- `attributes-and-methods.py` - Instance vs class attributes
- `constructor.py` - Object initialization

---

### 2. Constructors

**File:** `constructor.py`

Constructors (`__init__`) are special methods that initialize objects when they're created.

```python
class Student:
    def __init__(self, name, rollNumber):
        self.name = name
        self.rollNumber = rollNumber
```

**Types:**
- **Default Constructor**: No parameters (except self)
- **Parameterized Constructor**: Takes arguments to initialize attributes

---

### 3. Static Members

**Files:** `counter-static.py`, `static-practice.py`

Static members belong to the class rather than instances.

```python
class Counter:
    count = 0  # Class variable (static)
    
    @staticmethod
    def increment():
        Counter.count += 1
```

**Use Cases:**
- Shared data across all instances
- Utility functions that don't need instance data
- Factory methods

---

### 4. Access Specifiers

**File:** `access-specifier.py`

Python uses naming conventions for access control:

| Type | Syntax | Access |
|------|--------|--------|
| Public | `name` | Accessible everywhere |
| Protected | `_name` | Accessible in class and subclasses |
| Private | `__name` | Accessible only within the class |

```python
class Student:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"
```

---

## The Four Pillars of OOP

### 1. Encapsulation 🔒

**Files:** `encapsulation.py`, `bank-account-encapsulation.py`

Encapsulation is bundling data and methods together while restricting direct access to some components.

#### Real-World Example: Library Book Management

```python
class Book:
    def __init__(self, titles, authors, isAvailable):
        self.title = titles              # Public
        self.author = authors            # Public
        self.__isAvailable = isAvailable # Private
    
    def borrowBook(self, bookName):
        # Access controlled through methods
        for i in range(len(self.title)):
            if self.title[i] == bookName:
                if self.__isAvailable[i]:
                    self.__isAvailable[i] = False
                    return
                else:
                    print("Book is not available.")
    
    def getAvailability(self, bookName):
        # Controlled access to private data
        for i in range(len(self.title)):
            if self.title[i] == bookName:
                return self.__isAvailable[i]
```

**Benefits:**
- Data protection from unauthorized access
- Controlled modification through methods
- Internal implementation can change without affecting external code
- Better maintainability

**Key Principle:** Hide the internal state and require all interaction through methods (getters/setters).

---

### 2. Inheritance 👪

**Files:** `inheritance.py`, `inheritance-example.py`, `employee-inheritance.py`, `product-inheritance.py`

Inheritance allows a class to acquire properties and methods from another class.

#### Types of Inheritance

**Single Inheritance**
```python
class School:
    def __init__(self, schoolName):
        self.__schoolName = schoolName
    
    def getSchoolName(self):
        return self.__schoolName

class Student(School):  # Student inherits from School
    def __init__(self, studentName, schoolName):
        super().__init__(schoolName)
        self.__studentName = studentName
```

**Multi-level Inheritance**
```python
class School:
    pass

class Student(School):
    pass

class Parent(Student):  # Parent → Student → School
    pass
```

**Hierarchical Inheritance**
```python
class School:
    pass

class Student(School):  # Multiple classes inherit from School
    pass

class Teacher(School):
    pass
```

**Multiple Inheritance** (Not recommended in most cases)
```python
class A:
    pass

class B:
    pass

class C(A, B):  # Inherits from both A and B
    pass
```

**Benefits:**
- Code reusability
- Establishes IS-A relationships
- Promotes hierarchical organization
- Method overriding for polymorphism

---

### 3. Polymorphism 🎭

**File:** `polymorphism.py`

Polymorphism means "many forms" - the ability of different objects to respond to the same message in different ways.

#### Types of Polymorphism

**1. Compile-Time Polymorphism (Method Overloading)**

Python doesn't support traditional method overloading, but achieves similar behavior:

```python
class Calculator:
    def sum(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.sum(1, 2))      # 3
print(calc.sum(1, 2, 3))   # 6
```

**2. Runtime Polymorphism (Method Overriding)**

```python
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):  # Overrides parent method
        print("Woof")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Same method call, different behaviors
animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()  # Polymorphic behavior
```

**Benefits:**
- Flexibility in code
- Easier to extend functionality
- Cleaner, more intuitive code
- Supports duck typing in Python

---

### 4. Abstraction 🎨

**Files:** `abstraction.py`, `practice-abstraction.py`

Abstraction hides complex implementation details and shows only essential features.

```python
from abc import ABC, abstractmethod

class Car(ABC):  # Abstract class
    @abstractmethod
    def start(self):
        pass  # Must be implemented by subclasses
    
    @abstractmethod
    def stop(self):
        pass
    
    def horn(self):  # Concrete method
        print("Beep")

class ManualCar(Car):
    def start(self):
        print("Manual start with clutch")
    
    def stop(self):
        print("Apply brakes and clutch")

class AutomaticCar(Car):
    def start(self):
        print("Push button start")
    
    def stop(self):
        print("Apply brakes")
```

**Key Points:**
- Abstract classes cannot be instantiated
- Abstract methods must be implemented by subclasses
- Provides a contract that subclasses must follow
- Focuses on WHAT an object does, not HOW

**Benefits:**
- Reduces complexity by hiding unnecessary details
- Enforces a contract for subclasses
- Improves code maintainability
- Enables focusing on high-level functionality

---

## Advanced Concepts

### Interfaces

**Files:** `interfaces.py`, `multiple-interfaces.py`, `payment-interface.py`

In Python, interfaces are implemented using Abstract Base Classes (ABC).

```python
from abc import ABC, abstractmethod

class CarInterface(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        pass

class ManualCar(CarInterface):
    def start(self):
        print("Start the car")
    
    def stop(self):
        print("Stop the car")
    
    def accelerate(self):
        print("Accelerate the car")
```

**Interface vs Abstract Class:**

| Feature | Interface | Abstract Class |
|---------|-----------|----------------|
| Methods | All abstract | Can have concrete methods |
| Purpose | Define contract | Partial implementation |
| Inheritance | Multiple interfaces | Single abstract class |

**Real-World Example:** Payment Gateway (`payment-interface.py`)
- Different payment methods (Credit Card, PayPal, Crypto)
- All implement the same interface
- Easy to add new payment methods

---

### Inner Classes

**Files:** `inner-class.py`, `inner-practice.py`

A class defined inside another class.

```python
class Outer:
    def __init__(self):
        self.name = "Outer"
        self.inner = self.Inner()
    
    class Inner:
        def __init__(self):
            self.name = "Inner"
        
        def display(self):
            print("Inner class method")

# Usage
outer = Outer()
outer.inner.display()
```

**Use Cases:**
- Logical grouping of classes
- Improved encapsulation
- More readable and maintainable code
- Helper classes that are only used by outer class

---

### Generics

**File:** `generics.py`

Generics allow writing flexible, reusable code that works with multiple types.

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content
    
    def get_content(self) -> T:
        return self.content

# Can be used with any type
int_box = Box[int](123)
str_box = Box[str]("Hello")
```

**Benefits:**
- Type safety
- Code reusability
- Better IDE support and autocomplete
- Catch type errors at development time

---

### Object Cloning

**Files:** `object-cloning.py`, `practice-object-cloning.py`

Creating copies of objects - shallow vs deep copy.

```python
import copy

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # Mutable object

# Shallow copy - references are shared
person1 = Person("John", ["123 Main St"])
person2 = copy.copy(person1)
person2.address[0] = "456 Oak Ave"  # Affects both!

# Deep copy - complete independent copy
person3 = copy.deepcopy(person1)
person3.address[0] = "789 Elm St"  # Only affects person3
```

**When to Use:**
- Shallow: When you need a new object but can share references
- Deep: When you need completely independent objects

---

## Object Relationships

**File:** `assoiciation-aggregation-composition.py`

### 1. Association

A general relationship where objects are independent.

**Types:**

**One-to-One**
```python
class Passport:
    def __init__(self, number):
        self.number = number

class Person:
    def __init__(self, name, passport):
        self.name = name
        self.passport = passport  # HAS-A relationship
```

**One-to-Many**
```python
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class College:
    def __init__(self, name):
        self.name = name
        self.students = []  # One college, many students
    
    def addStudent(self, student):
        self.students.append(student)
```

**Many-to-Many**
```python
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []  # Many students
    
    def addCourse(self, course):
        self.courses.append(course)

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []  # Many courses
    
    def addStudent(self, student):
        self.students.append(student)
```

---

### 2. Aggregation (Weak Relationship)

**File:** `practice-aggregation.py`

Objects can exist independently. "Has-A" relationship where the contained object can exist without the container.

```python
class Engine:
    def __init__(self, type):
        self.type = type

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # Car HAS-A Engine
    
# Engine exists independently
engine = Engine("V8")
car = Car("Mustang", engine)
del car  # Car is destroyed, but engine still exists
```

**Characteristics:**
- Weak relationship
- Child can exist without parent
- Represented by hollow diamond in UML

---

### 3. Composition (Strong Relationship)

**File:** `practice-composition.py`

Strong "owns-A" relationship where the contained object cannot exist without the container.

```python
class Engine:
    def __init__(self, type):
        self.type = type

class Car:
    def __init__(self, model, engine_type):
        self.model = model
        self.engine = Engine(engine_type)  # Car OWNS Engine
    
# Engine is created within Car
car = Car("Mustang", "V8")
del car  # Engine is destroyed with the car
```

**Characteristics:**
- Strong relationship
- Child cannot exist without parent
- Parent owns child's lifecycle
- Represented by filled diamond in UML

---

### Comparison Table

| Feature | Aggregation | Composition |
|---------|-------------|-------------|
| Relationship | Weak | Strong |
| Lifecycle | Independent | Dependent |
| Example | Car and Engine (separate) | Car and Engine (internal) |
| Deletion | Child survives | Child destroyed |
| UML Symbol | Hollow diamond | Filled diamond |

---

## Additional Features

### File Handling

**File:** `file-handling.py`

Working with files in an OOP context.

```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename
    
    def write(self, content):
        with open(self.filename, 'w') as f:
            f.write(content)
    
    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()
```

**Operations Covered:**
- Reading files
- Writing files
- Appending content
- File operations with context managers

---

### Exception Handling

**File:** `execption-handling.py`

Handling errors gracefully in OOP.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient funds")
            self.balance -= amount
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print(f"Current balance: {self.balance}")
```

**Best Practices:**
- Use specific exceptions
- Handle errors at appropriate level
- Always clean up resources (use `finally`)
- Create custom exceptions for domain-specific errors

---

## File Index

### By Category

**Core Concepts (Beginner)**
1. `classes-and-objects.py` - Basic class and object creation
2. `constructor.py` - Object initialization
3. `attributes-and-methods.py` - Instance and class members
4. `access-specifier.py` - Public, protected, private

**Four Pillars**
5. `encapsulation.py` - Basic encapsulation
6. `bank-account-encapsulation.py` - Real-world encapsulation example
7. `inheritance.py` - Basic inheritance concepts
8. `inheritance-example.py` - Practical inheritance examples
9. `employee-inheritance.py` - Employee hierarchy
10. `product-inheritance.py` - Product categorization
11. `polymorphism.py` - Method overriding and polymorphism
12. `abstraction.py` - Abstract classes and methods
13. `practice-abstraction.py` - Additional abstraction examples

**Interfaces**
14. `interfaces.py` - Basic interface implementation
15. `multiple-interfaces.py` - Multiple interface implementation
16. `payment-interface.py` - Payment gateway example

**Object Relationships**
17. `assoiciation-aggregation-composition.py` - All relationships
18. `practice-aggregation.py` - Aggregation examples
19. `practice-composition.py` - Composition examples

**Advanced Topics**
20. `static-practice.py` - Static members and methods
21. `counter-static.py` - Static variable example
22. `inner-class.py` - Nested classes
23. `inner-practice.py` - Inner class practice
24. `generics.py` - Generic programming
25. `object-cloning.py` - Shallow and deep copy
26. `practice-object-cloning.py` - Cloning practice

**Practical Examples**
27. `shape-calculator.py` - Geometry calculations
28. `file-handling.py` - File I/O operations
29. `execption-handling.py` - Error handling

**Miscellaneous**
30. `solid.py` - SOLID principles overview

---

## Learning Roadmap

### Phase 1: Foundations (Week 1)

**Goal:** Understand basic OOP concepts

1. Start with `classes-and-objects.py`
2. Learn constructors: `constructor.py`
3. Understand attributes: `attributes-and-methods.py`
4. Study access specifiers: `access-specifier.py`

**Practice:** Create your own classes (Student, Book, Product)

---

### Phase 2: The Four Pillars (Week 2-3)

**Goal:** Master fundamental OOP principles

#### Encapsulation
1. `encapsulation.py`
2. `bank-account-encapsulation.py`

#### Inheritance
3. `inheritance.py`
4. `inheritance-example.py`
5. `employee-inheritance.py`

#### Polymorphism
6. `polymorphism.py`

#### Abstraction
7. `abstraction.py`
8. `practice-abstraction.py`

**Practice:** Build a simple library management system

---

### Phase 3: Advanced Concepts (Week 4-5)

**Goal:** Learn advanced OOP features

1. **Interfaces**
   - `interfaces.py`
   - `multiple-interfaces.py`
   - `payment-interface.py`

2. **Relationships**
   - `assoiciation-aggregation-composition.py`
   - `practice-aggregation.py`
   - `practice-composition.py`

3. **Special Features**
   - `static-practice.py`
   - `inner-class.py`
   - `generics.py`
   - `object-cloning.py`

**Practice:** Design a complex system (e-commerce, social media)

---

### Phase 4: Practical Application (Week 6+)

**Goal:** Apply OOP to real-world scenarios

1. File operations: `file-handling.py`
2. Error handling: `execption-handling.py`
3. Review SOLID principles: `solid.py` + `/solid/` folder
4. Build projects combining multiple concepts

**Project Ideas:**
- Banking system with accounts, transactions, and reports
- Library management with books, members, and borrowing
- E-commerce platform with products, cart, and orders
- Task management system with users, projects, and tasks

---

## Design Principles

### When to Use Each OOP Feature

| Feature | Use When... |
|---------|-------------|
| **Encapsulation** | Always - protect data and control access |
| **Inheritance** | IS-A relationship exists (Car IS-A Vehicle) |
| **Polymorphism** | Multiple types should handle same message differently |
| **Abstraction** | Need to define contracts or hide implementation details |
| **Interfaces** | Multiple unrelated classes share common behavior |
| **Aggregation** | Objects can exist independently (Car-Driver) |
| **Composition** | Object lifecycle is tied to parent (Car-Engine) |

---

## Common Pitfalls

### 1. Over-inheritance
**Problem:** Deep inheritance hierarchies are hard to maintain
**Solution:** Prefer composition over inheritance

### 2. God Objects
**Problem:** Classes that do too much
**Solution:** Follow Single Responsibility Principle

### 3. Tight Coupling
**Problem:** Classes depend too heavily on each other
**Solution:** Use interfaces and dependency injection

### 4. Ignoring Encapsulation
**Problem:** Direct access to internal state
**Solution:** Use getters/setters and private attributes

### 5. Misusing Inheritance
**Problem:** Using inheritance for code reuse when there's no IS-A relationship
**Solution:** Use composition instead

---

## Interview Preparation

### Common Questions

**1. What is OOP?**
- Paradigm organizing code around objects
- Four pillars: Encapsulation, Inheritance, Polymorphism, Abstraction
- Benefits: modularity, reusability, maintainability

**2. Explain Encapsulation**
- Bundling data and methods
- Hiding internal state
- Controlled access through methods
- Example: `Bank Account` with private balance

**3. Difference between Abstraction and Encapsulation**
- Abstraction: Hide complexity, show only essential features
- Encapsulation: Hide data, provide controlled access
- Abstraction uses abstraction, encapsulation uses access modifiers

**4. Composition vs Inheritance**
- Inheritance: IS-A relationship (Dog IS-A Animal)
- Composition: HAS-A relationship (Car HAS-A Engine)
- Prefer composition for flexibility

**5. Polymorphism Types**
- Compile-time: Method overloading (Python uses default arguments)
- Runtime: Method overriding (subclass changes parent behavior)

### Coding Questions

Practice implementing:
1. **Library Management System** (encapsulation, relationships)
2. **Shape Hierarchy** (inheritance, polymorphism, abstraction)
3. **Payment Gateway** (interfaces, polymorphism)
4. **Vehicle System** (inheritance, composition)
5. **Employee Management** (all concepts combined)

---

## Best Practices

1. **Follow SOLID Principles** - See `/solid/README.md`
2. **Use meaningful names** - Classes are nouns, methods are verbs
3. **Keep classes focused** - Single Responsibility
4. **Favor composition over inheritance** - More flexible
5. **Program to interfaces** - Not implementations
6. **Encapsulate what varies** - Protect changing parts
7. **Document your code** - Explain the WHY, not the WHAT
8. **Write testable code** - Loose coupling, high cohesion

---

## Additional Resources

### Books
- "Clean Code" by Robert C. Martin
- "Design Patterns" by Gang of Four
- "Head First Object-Oriented Analysis and Design"

### Online Resources
- [Python OOP Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [Refactoring Guru - OOP Concepts](https://refactoring.guru/design-patterns/what-is-pattern)

### Related Topics
- Design Patterns (Creational, Structural, Behavioral)
- SOLID Principles (see `/solid/` folder)
- Clean Code Principles
- Domain-Driven Design (DDD)

---

## Quick Reference

### Python OOP Syntax

```python
# Class definition
class ClassName:
    class_variable = "shared"
    
    def __init__(self, param):
        self.instance_variable = param
    
    def instance_method(self):
        return self.instance_variable
    
    @classmethod
    def class_method(cls):
        return cls.class_variable
    
    @staticmethod
    def static_method():
        return "No access to instance or class"

# Inheritance
class Child(Parent):
    def __init__(self):
        super().__init__()

# Multiple inheritance
class Child(Parent1, Parent2):
    pass

# Abstract class
from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod
    def must_implement(self):
        pass

# Property decorators
class Example:
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        self._value = val
```

---

**Last Updated:** January 2026  
**Total Files:** 30+  
**Language:** Python 3.x  
**Purpose:** Learning, Practice, Interview Preparation

For SOLID principles, see [/solid/README.md](../solid/README.md)
