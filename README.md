# Python Modules

These are a series of projects designed to introduce the Python programming language and its interface. They are designed to be thematic implementations of specific more complex themes. 

## Module Breakdown

 - **Module 00 (** *v 1.0* **):** Introduction to core Python concepts, including variables, functions, data input/output, control flow (`if`, `while`, `for`, `range`), basic recursion, helper functions, and type annotations.

 - **Module 01 (** *v 2.1* **):** Introduction to Python programming with a focus on object-oriented design. Covers class construction (constructors and methods), encapsulation and data protection, getters and setters, inheritance using `super()`, basic composition, and the use of decorators such as `@classmethod` and `@staticmethod`. Also introduces executable script structure with `if __name__ == "__main__":`.  
 
 - **Module 02 (** *v 2.1* **):** Introduction to error handling in Python using `try`, `except`, and `finally` blocks. Focus on raising and managing exceptions (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `KeyError`) and designing custom exception classes with meaningful error messages. Emphasis on building resilient programs that handle failures gracefully while maintaining system stability

- **Module 03 (** *v 2.2* **):** Introduction to the `sys` module for handling command-line input (`sys.argv`). Applied core Python collections (`list`, `set`, `dict`) for data processing and analytics tasks. Implemented memory-efficient data streaming with `generators` and practiced advanced data transformation using `list`, `dict`, and `set comprehensions`.

- **Module 04 (** *v 2.1* **):** Introcution to file handling and secure resource management using the `with` statement. Implementing error handling with exceptions such as `FileNotFoundError`, `PermissionError`, and `OSError`. Introduction to system-level communication through the `sys` module, working with `sys.stdin`, `sys.stdout`, and `sys.stderr` to properly separate input, standard output, and alert output channels.

- **Module 05 (** *v 2.0* **):** Introcution to advanced object-oriented design using `ABC`and `@abstractmethod` to define abstract base classes and enforce implementation contracts. Applied **method overriding** and **subtype polymorphism** to git rm -r $(find . -type d -name "__pycache__") 
fatal: No pathspec was given. Which files should I remove?
build flexible processing systems. Implemented interface-driven design using `Protocol` for duck typing, combining inheritance and composition to create scalable, multi-stage data pipelines with structured error handling and polymorphic orchestration.

- **Module 06 (** *v 1.1* **):** Introduction to Python package architecture through the use of `__init__.py` files. Learned how to import objects from custom modules using `from ... import`, and understood the difference between **absolute imports** and **relative imports**. Avoiding **circular dependencies**, using strategies like **late imports**, **dependency injection**, **shared modules**.

- **Module 07 (** *v 2.0* **):** Applying the concept of abstract base classes and using multiple inheritance for implementing multiple interfaces. Focuses on combining independent behaviors into cohesive systems, enabling flexible architecture through interface composition and polymorphism.

- **Module 08 (** *v 2.0* **):** Introduction to **data  engineering workflows** and **environment configuration** in Python, dependency managment using **pip** and **Poetry**, including the creation of `requirements.txt`and `pyproject.toml` files for reproducible environments. Introduction to data processing and visualization using **NumPy**, **Pandas**, and **Matplotlib**, as well as interaction with external services through **HTTP APIs** using `requests`library. Configuration management with **environment variables** and `.env`files using **python-dotenv**, demonstrating development vs production settings and configuration validation.

- **Module 09 (** *v 2.0* **):** Introduction to **data validation** and **structured data modeling** using **Pydantic**. Designed validated models using field constraints, enumerations, and optional fields. Implemented custom business logic validation with `@model_validator` to enforce complex rules across model fields.

- **Module 10 (** *v 2.0* **):** Introduction to **functional programming** in Python: **lambdas**, **higher-order functions**, **closures**, **decorators**, and advanced utilities from the functools module (reduce, partial, lru_cache, singledispatch).