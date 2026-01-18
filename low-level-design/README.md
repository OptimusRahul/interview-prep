# Low-Level Design (LLD)

A comprehensive collection of Low-Level Design concepts, principles, and patterns implemented in Python. This repository covers fundamental Object-Oriented Programming (OOP) concepts and SOLID principles with practical examples.

## Table of Contents

- [Overview](#overview)
- [Structure](#structure)
- [Topics Covered](#topics-covered)
- [Getting Started](#getting-started)
- [Usage](#usage)

## Overview

This repository is designed to help understand and practice low-level design concepts that are essential for:
- Writing maintainable and scalable code
- System design interviews
- Building robust software applications
- Following best practices in software engineering

## Structure

```
low-level-design/
├── oops/           # Object-Oriented Programming concepts
├── solid/          # SOLID principles with examples
└── README.md       # This file
```

## Topics Covered

### Object-Oriented Programming (OOP)

The `oops/` directory contains 30+ Python files covering core OOP concepts:

#### Core Concepts
- **Classes and Objects** - Basic building blocks of OOP
- **Constructors** - Object initialization
- **Attributes and Methods** - Instance and class-level members
- **Static Members** - Class-level variables and methods

#### Four Pillars of OOP
1. **Encapsulation**
   - `encapsulation.py` - Basic encapsulation concepts
   - `bank-account-encapsulation.py` - Real-world banking example
   - `access-specifier.py` - Public, private, and protected members

2. **Inheritance**
   - `inheritance.py` - Basic inheritance
   - `inheritance-example.py` - Practical examples
   - `employee-inheritance.py` - Employee hierarchy example
   - `product-inheritance.py` - Product categorization example

3. **Polymorphism**
   - `polymorphism.py` - Method overriding and runtime polymorphism

4. **Abstraction**
   - `abstraction.py` - Abstract classes and methods
   - `practice-abstraction.py` - Additional practice examples

#### Advanced Concepts
- **Interfaces** - Contract-based programming
  - `interfaces.py`
  - `multiple-interfaces.py`
  - `payment-interface.py` - Real-world payment gateway example

- **Relationships**
  - `assoiciation-aggregation-composition.py` - Object relationships
  - `practice-aggregation.py` - Has-a relationship
  - `practice-composition.py` - Strong ownership relationship

- **Other Features**
  - `generics.py` - Generic programming
  - `object-cloning.py` - Deep and shallow copying
  - `inner-class.py` - Nested classes
  - `file-handling.py` - File I/O operations
  - `execption-handling.py` - Error handling patterns

### SOLID Principles

The `solid/` directory contains implementations of all five SOLID principles:

| Principle | File | Description |
|-----------|------|-------------|
| **S**ingle Responsibility | `srp.py` | A class should have one reason to change |
| **O**pen/Closed | `ocp.py` | Open for extension, closed for modification |
| **L**iskov Substitution | `lsp.py` | Subtypes must be substitutable for base types |
| **I**nterface Segregation | `isp.py` | No client should depend on unused methods |
| **D**ependency Inversion | `dip.py` | Depend on abstractions, not concretions |

Each file includes:
- Violation examples showing what NOT to do
- Corrected solutions following the principle
- Real-world use cases with practical examples

See [solid/README.md](solid/README.md) for detailed explanations.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Basic understanding of Python syntax

### Running the Examples

1. Navigate to the directory:
```bash
cd /Users/ghost/Developer/dsa/low-level-design
```

2. Run any example file:
```bash
# OOP examples
python3 oops/encapsulation.py
python3 oops/inheritance.py

# SOLID principles
python3 solid/srp.py
python3 solid/ocp.py
```

## Usage

### Learning Path

**For Beginners:**
1. Start with `oops/classes-and-objects.py`
2. Progress through the four pillars: encapsulation → inheritance → polymorphism → abstraction
3. Move to advanced concepts like interfaces and relationships
4. Finally, study SOLID principles in the `solid/` directory

**For Interview Preparation:**
1. Review all SOLID principles examples
2. Focus on real-world examples in each category
3. Practice explaining violations vs. solutions
4. Implement your own examples based on the patterns

### Best Practices

Each file demonstrates:
- Common mistakes and violations
- Correct implementations
- Real-world scenarios
- Practical use cases

## Contributing

Feel free to add more examples or improve existing ones. When adding new files:
- Follow the existing naming conventions
- Include both violation and solution examples
- Add comments explaining the concepts
- Provide practical, real-world examples

## Resources

- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Design Patterns](https://refactoring.guru/design-patterns)

## License

This is a personal learning repository. Feel free to use it for educational purposes.

---

**Last Updated:** January 2026
