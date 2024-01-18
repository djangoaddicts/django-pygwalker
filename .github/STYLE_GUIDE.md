# Project Style Guide

This Python style guide provides conventions and best practices for writing clean and maintainable Python code. Adhering to these guidelines will help ensure consistency across projects and enhance the clarity, maintainability, 
and readability of the code.

## Table of Contents
- [PEP 8](#pep-8)
- [Line Length](#line-length)
- [Naming Conventions](#naming-conventions)
- [Docstrings](#docstrings)
- [Typing](#typing)
- [Virtual Environments](#virtual-environments)

<br/>

## PEP 8

Adhere to the PEP 8 style guide, which is the style guide for Python code. Please make sure to familiarize yourself with PEP 8 guidelines: [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).

<br/>

## Line Length

The maximum line length for code and comments is set to 120 characters. This allows for better readability without excessively long lines.

<br/>

## Naming Conventions

### Classes 
- Class names should follow the CamelCase convention.
- Class names should be descriptive and represent a clear concept or object.

    Example:

    ```python
    class Calculator:
        def __init__(self):
            # Constructor implementation

        def add(self, x, y):
            # Method implementation
    ```

### Functions
- Function names should be lowercase, with words separated by underscores.
- Function names should begin with a verb to indicate the action or operation they perform.

    Examples: 

    ```python
    def calculate_sum(numbers):
        """Calculate the sum of a list of numbers."""
        # Function implementation

    def validate_input(user_input):
        """Validate user input and return True if valid, False otherwise."""
        # Function implementation

    def process_data(data):
        """Process the given data and return the result."""
        # Function implementation
    ```

### Variables
Choosing meaningful and consistent variable names is essential for code readability. Follow these conventions:

- Use lowercase letters with underscores for variable names (snake_case).
- Be descriptive and use meaningful names to indicate the purpose of the variable.

    Examples:

    ```python
    # Good variable names
    user_name = "John"
    num_items = 5
    total_amount = 100.50

    # Avoid ambiguous or single-letter names
    a = "John"  # Not recommended
    n = 5       # Not recommended
    ```


- Constants should be in uppercase with underscores.

    Examples:

    ```python
    MAX_RETRIES = 3
    PI = 3.14159
    ```

- Avoid using names that shadow built-in functions or keywords.

    Example:

    ```python
    # Bad: Don't use 'list' as a variable name
    list = [1, 2, 3]

    # Good: Choose a different name
    my_list = [1, 2, 3]
    ```

- Use meaningful prefixes and suffixes for variable names where applicable.

    Example:

    ```python
    # Prefix 'is_' for boolean variables
    is_valid = True

    # Suffix iterators with type (such as '_list')
    name_list = ["John", "Mary", "Robert", "Sue"]
    ```

<br/>

## Docstrings

Documenting your code is crucial for understanding its functionality and usage. Use Google-style docstrings to provide clear and concise documentation.

### Module Docstring
- Include a module-level docstring at the beginning of each Python file.
- Use triple double-quotes for multi-line docstrings.

    Example:

    ```python
    """Module-level docstring.

    This module provides utility functions for handling calculations.
    """

    # Rest of the module code
    ```

### Class Docstring
- Include a class-level docstring immediately below the class definition.
- Briefly describe the purpose and usage of the class.

    Example:

    ```python
    class Calculator:
        """A simple calculator class.

        This class provides basic arithmetic operations such as addition and subtraction.
        """

        def __init__(self):
            # Constructor implementation
    ```

### Function Docstring
- Include a function-level docstring immediately below the function definition.
- Provide a clear description of the function's purpose, parameters, and return values.

    Example:

    ```python
    def calculate_sum(numbers):
        """Calculate the sum of a list of numbers.

        Args:
            numbers (list): A list of numerical values.

        Returns:
            float: The sum of the input numbers.
        """
        # Function implementation

    ```

<br/>

## Typing
Python's optional type hints, introduced in PEP 484 and expanded in subsequent PEPs, provide a way to statically indicate the type of variables and function parameters. Proper use of typing can enhance code readability, maintainability, and catch certain types of errors early in the development process.

### General Guidelines
1. **Use Type Hints:**

    Type hints should be used consistently to indicate the expected types of variables and function parameters.

    Example:
    
    ```python
    def add_numbers(a: int, b: int) -> int:
        return a + b
    ```

2. **Avoid Redundant Type Hints:**

    Avoid providing type hints when the type is obvious from the variable name or the context.

    Example:
    
    ```python
    # Good
    name: str = "John"

    # Avoid unnecessary type hint
    age = 30  # Type is clear without specifying it
    ```

3. **Use Expressive Variable Names:**

    Choose variable names that convey meaning and make type hints redundant.

    Example:

    ```python
    def calculate_area(length: float, width: float) -> float:
        return length * width
    ```

4. **Be Consistent with Typing Styles:**

    Choose a consistent style for type hints, either using the ```:``` notation or the ```->``` notation for function return types.

    Example:

    ```python
    # Consistent style with `:`
    def greet(name: str) -> None:
        print(f"Hello, {name}!")

    # Consistent style with `->`
    def multiply(a: int, b: int) -> int:
        return a * b
    ```

### Specific Typing Practices

1. **Type Annotations for Variables:**

    Use type annotations for variables, especially in cases where the type might not be immediately obvious.

    Example:

    ```python
    count: int = 0
    ```

2. **Type Annotations for Function Parameters and Return Types:**

    Clearly annotate the types of function parameters and return types.

    Example:

    ```python
    def calculate_total(items: List[float]) -> float:
        return sum(items)
    ```

3. **Type Aliases:**

    Use typing module aliases to create readable and self-documenting type aliases for complex types.

    Example:

    ```python
    from typing import List, Tuple

    Coordinates = Tuple[float, float]
    PointList = List[Coordinates]

    def plot_points(points: PointList) -> None:
        # Plotting logic here
    ```

4. **Union Types:**

    Use Union types when a variable or parameter can have multiple types.
    
    Example:

    ```python
    from typing import Union

    def display_value(value: Union[int, float, str]) -> None:
        print(value)
    ```

5. **Type Hinting in Generics:**

    Use generic types when working with containers or collections.

    Example:

    ```python
    from typing import List, Tuple

    def process_data(data: List[Tuple[str, int]]) -> None:
        # Processing logic here
    ```

6. **Callable Types:**

    Clearly annotate callable types using Callable from the typing module.


    Example:

    ```python
    from typing import Callable

    def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
        return func(a, b)
    ```

<br/>

## Virtual Environments

### Introduction

A virtual environment is a self-contained directory that contains a Python interpreter and allows you to install and manage project-specific dependencies. Use a virtual environment to isolate project dependencies and avoid conflicts with system-wide packages.


### Creating a Virtual Environment
To create a virtual environment, use the following command at the **root** of the repository:

```shell
python -m venv venv
```

### Activating the Virtual Environment
Once the virtual environment is created, activate it using the appropriate command for your operating system:

For Windows:

```shell
venv\Scripts\activate
```

For Mac, Linux, and WSL:

```shell
source venv/bin/activate
```

<br/>
