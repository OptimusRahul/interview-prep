# SOLID Principles

A comprehensive guide to SOLID design principles with Python implementations. Each principle is demonstrated with violation examples and corrected solutions using real-world scenarios.

## Table of Contents

- [What are SOLID Principles?](#what-are-solid-principles)
- [Why SOLID?](#why-solid)
- [Principles Overview](#principles-overview)
- [Detailed Examples](#detailed-examples)
- [Quick Reference](#quick-reference)

## What are SOLID Principles?

SOLID is an acronym for five design principles that make software designs more understandable, flexible, and maintainable. These principles were promoted by Robert C. Martin (Uncle Bob) and are fundamental to object-oriented design.

## Why SOLID?

Following SOLID principles helps you:
- Write code that's easier to maintain and extend
- Reduce coupling between components
- Improve code testability
- Make systems more resilient to change
- Create more reusable components

## Principles Overview

| Principle | Key Concept | Main Benefit |
|-----------|-------------|--------------|
| **S**RP | One class, one responsibility | Easier maintenance |
| **O**CP | Extend without modifying | Safer additions |
| **L**SP | Subtypes are substitutable | Reliable inheritance |
| **I**SP | Lean interfaces | Flexible implementation |
| **D**IP | Depend on abstractions | Loose coupling |

## Detailed Examples

### 1. Single Responsibility Principle (SRP)

**File:** `srp.py`

**Principle:** A class should have only one reason to change.

#### Violation Example
```python
class SalaryCalculatorVoilation:
    def calculate_salary(self, hours_worked, hourly_rate):
        return hours_worked * hourly_rate
    
    def generate_report(self, salary):
        # Violates SRP - mixing calculation and reporting
        print(f"Salary report: {salary}")
```

**Problem:** This class has two responsibilities - calculating salary and generating reports.

#### Solution
```python
class SalaryCalculator:
    def calculate_salary(self, hours_worked, hourly_rate):
        return hours_worked * hourly_rate

class ReportGenerator:
    def generate_report(self, salary):
        print(f"Salary report: {salary}")
```

**Benefit:** Each class has a single, well-defined responsibility.

---

### 2. Open/Closed Principle (OCP)

**File:** `ocp.py`

**Principle:** Classes should be open for extension but closed for modification.

#### Violation Example
```python
class InvoiceCalculatorVoilation:
    def calculateTotal(self, region, amount):
        if region == "IN":
            return amount * 1.05
        elif region == "US":
            return amount * 1.05
        elif region == "EU":
            return amount * 1.05
        # Need to modify this class to add new regions
```

**Problem:** Adding a new region requires modifying existing code.

#### Solution
```python
class InvoiceCalculator(ABC):
    @abstractmethod
    def calculateTotal(self, amount):
        pass

class INInvoiceCalculator(InvoiceCalculator):
    def calculateTotal(self, amount):
        return amount * 1.05

class USInvoiceCalculator(InvoiceCalculator):
    def calculateTotal(self, amount):
        return amount * 1.05

# Can add new regions without modifying existing code
```

**Benefit:** New tax regions can be added by creating new classes, not modifying existing ones.

---

### 3. Liskov Substitution Principle (LSP)

**File:** `lsp.py`

**Principle:** Objects of a superclass should be replaceable with objects of subclasses without breaking the application.

#### Real-World Examples

**Violation:** Square inheriting from Rectangle
- When you set width=5 and height=10 on a Rectangle, you expect area=50
- But if it's actually a Square, the area would be 100
- This breaks the expected behavior!

**Solution:** Use a common `Shape` interface
- Both Rectangle and Square inherit from Shape
- Each implements its own `getArea()` method correctly
- No unexpected behavior when substituting one for another

**Additional Example:** Notification System
```python
class Notification:
    def sendNotification(self):
        print("Notification sent")

class EmailNotification(Notification):
    def sendNotification(self):
        print("Email Notification sent")

class SMSNotification(Notification):
    def sendNotification(self):
        print("SMS Notification sent")
```

**Benefit:** Any notification type can be used interchangeably without breaking functionality.

---

### 4. Interface Segregation Principle (ISP)

**File:** `isp.py`

**Principle:** No client should be forced to depend on methods it does not use.

#### Violation Example: Uber App
```python
class UberUser(ABC):
    @abstractmethod
    def bookRide(self):      # Riders need this
        pass
    
    @abstractmethod
    def acceptRide(self):    # Drivers need this
        pass
    
    @abstractmethod
    def trackEarnings(self):  # Drivers need this
        pass
    
    @abstractmethod
    def rateDriver(self):    # Riders need this
        pass
```

**Problem:** 
- Riders are forced to implement `acceptRide()` and `trackEarnings()` (not needed)
- Drivers are forced to implement `bookRide()` and `rateDriver()` (not needed)

#### Solution
```python
class RiderInterface(ABC):
    @abstractmethod
    def bookRide(self):
        pass
    
    @abstractmethod
    def rateDriver(self):
        pass

class DriverInterface(ABC):
    @abstractmethod
    def acceptRide(self):
        pass
    
    @abstractmethod
    def trackEarnings(self):
        pass
    
    @abstractmethod
    def ratePassenger(self):
        pass
```

**Benefit:** Each user type only implements the methods it actually needs.

---

### 5. Dependency Inversion Principle (DIP)

**File:** `dip.py`

**Principle:** High-level modules should not depend on low-level modules. Both should depend on abstractions.

#### Violation Example
```python
class RecentlyAdded:
    def getRecommendations(self):
        print("Showing recently added content...")

class RecommendationEngine:
    def __init__(self):
        self.recommender = RecentlyAdded()  # Tightly coupled!
    
    def recommend(self):
        self.recommender.getRecommendations()
```

**Problem:** The high-level `RecommendationEngine` is tightly coupled to the low-level `RecentlyAdded` class.

#### Solution
```python
class RecommendationStrategy(ABC):
    @abstractmethod
    def getRecommendations(self):
        pass

class RecentlyAdded(RecommendationStrategy):
    def getRecommendations(self):
        print("Showing recently added content...")

class TrendingNow(RecommendationStrategy):
    def getRecommendations(self):
        print("Showing trending content...")

class GenreBased(RecommendationStrategy):
    def getRecommendations(self):
        print("Showing content based on your favorite genres...")

class RecommendationEngine:
    def __init__(self, strategy: RecommendationStrategy):
        self.strategy = strategy  # Depends on abstraction
    
    def recommend(self):
        self.strategy.getRecommendations()
```

**Benefit:** Can switch recommendation strategies without modifying the engine.

---

## Quick Reference

### When to Apply Each Principle

| Principle | Apply When... |
|-----------|--------------|
| **SRP** | A class is doing too many things |
| **OCP** | You find yourself modifying existing code to add features |
| **LSP** | Inheritance hierarchies behave unexpectedly |
| **ISP** | Interfaces have methods that some implementers don't need |
| **DIP** | High-level logic depends on low-level implementation details |

### Common Violations to Watch For

- **SRP:** Classes with "and" in their name (e.g., `UserManagerAndValidator`)
- **OCP:** Multiple `if-elif-else` or `switch` statements for type checking
- **LSP:** Subclasses throwing "not implemented" exceptions
- **ISP:** Empty method implementations or methods that throw "not supported"
- **DIP:** Direct instantiation of concrete classes in high-level modules

### Red Flags in Code

```python
# SRP Violation
class User:
    def save_to_database(self): pass
    def send_email(self): pass
    def generate_report(self): pass

# OCP Violation
if type == "A": ...
elif type == "B": ...
elif type == "C": ...

# LSP Violation
class Bird:
    def fly(self): pass

class Penguin(Bird):
    def fly(self):
        raise Exception("Can't fly!")

# ISP Violation
class Worker(ABC):
    @abstractmethod
    def work(self): pass
    @abstractmethod
    def eat(self): pass

class Robot(Worker):
    def eat(self):
        pass  # Robots don't eat!

# DIP Violation
class HighLevel:
    def __init__(self):
        self.low = ConcreteLowLevel()  # Direct dependency
```

## Running the Examples

```bash
# Run individual principles
python3 srp.py
python3 ocp.py
python3 lsp.py
python3 isp.py
python3 dip.py
```

Each file includes:
1. Commented violation examples
2. Corrected solutions
3. Real-world use cases
4. Runnable code with output

## Interview Tips

When asked about SOLID principles:
1. **Explain the principle** in simple terms
2. **Give a real-world example** (not just code)
3. **Show both violation and solution**
4. **Explain the benefits** of following the principle
5. **Mention when NOT to over-engineer** (pragmatism matters)

## Resources

- [Robert C. Martin's Blog](http://blog.cleancoder.com/)
- [SOLID Principles Paper](https://web.archive.org/web/20150906155800/http://www.objectmentor.com/resources/articles/Principles_and_Patterns.pdf)
- [Refactoring Guru - SOLID](https://refactoring.guru/design-patterns/solid-principles)

---

**Last Updated:** January 2026
**Language:** Python 3.x
**Author:** Personal Learning Repository
