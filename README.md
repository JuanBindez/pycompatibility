# pycompatibility

![PyPI - Downloads](https://img.shields.io/pypi/dm/pycompatibility)
![PyPI - License](https://img.shields.io/pypi/l/pycompatibility)
![GitHub Tag](https://img.shields.io/github/v/tag/JuanBindez/pycompatibility?include_prereleases)
<a href="https://pypi.org/project/pycompatibility/"><img src="https://img.shields.io/pypi/v/pycompatibility" /></a>

## Python3 library for checking code compatibility with different Python versions.

#### is a tool designed to help verify the compatibility of Python code with versions older than Python 3.8. Specifically, this tool analyzes Python files for features introduced after Python 3.7 and provides refactoring suggestions to ensure that the code can run on older versions.


## Features

#### The pycompatibility detects and reports the use of the following features introduced after Python 3.7:

- 1. Walrus Operator (:=): Introduced in Python 3.8, this operator allows variable assignment within expressions. The tool detects its usage and suggests refactoring to avoid its use if maintaining compatibility with older versions is necessary.

- 2. Positional-Only Parameters: Introduced in Python 3.8, these parameters are defined with the / syntax. The tool alerts you to their use and recommends refactoring to ensure compatibility with Python 3.7.

- 3. Assignment Expressions in Comprehensions: Introduced in Python 3.9, these expressions allow variable assignment within comprehensions. The tool identifies these expressions and suggests alternatives.

- 4. Type Union Operator (|): Introduced in Python 3.10, this operator allows combining types in annotations. The tool detects the use of this operator and suggests replacing it with Optional from the typing module.

- 5. Structural Pattern Matching (match-case): Introduced in Python 3.10, structural pattern matching allows code to be organized based on patterns. The tool identifies this construct and suggests avoiding its use if compatibility with older versions is required.

- 6. Enhanced F-strings: F-strings were enhanced in Python 3.8. The tool detects the use of f-strings and provides refactoring suggestions if needed.


### Install

    pip install pycompatibility

### Command line just pass the name of the script as an argument which will show compatibility

    pycompatibility example_code.py


### In this example you can test a script that contains features that were introduced after version 3.7 of Python, this helps you maintain compatibility with older versions

#### script for testing "example_code.py"


```python
def example_function():
    x = 10
    y = (z := x + 5)  # Walrus operator (3.8+)
    print(f"The value of z is: {z}")  # f-string (3.6+)

    def inner_function(a: int | None):  # Type union operator (3.10+)
        if a is None:
            return "a is None"
        return f"a is {a}"

    result = inner_function(None)
    print(result)

    match result:  # Structural pattern matching (3.10+)
        case "a is None":
            print("Matched None")
        case _:
            print("Matched something else")

    items = [1, 2, 3, 4, 5]
    if any((n := x) > 3 for x in items):  # Walrus operator in comprehensions (3.9+)
        print(f"Found an item greater than 3: {n}")

    context = (open("file1.txt"), open("file2.txt"))  # Parenthesized context managers (3.9+)
    with context as (f1, f2):
        print(f1.read(), f2.read())

    def positional_only_func(a, b, /, c):  # Positional-only parameters (3.8+)
        print(a, b, c)

    positional_only_func(1, 2, 3)
    

```

#### Now just test the script as in the instruction below

```python

>>> from pycompatibility import CompatibilityChecker
>>> 
>>> checker = CompatibilityChecker("example_code.py")
>>> checker.verify()
Line 7: Use of the type union operator '|' detected. Introduced in Python 3.10+.
Suggestion: Replace 'int | None' with 'Optional[int]' from the 'typing' module.

Line 4: Use of the walrus operator ':=' detected. Introduced in Python 3.8+.
Suggestion: Refactor to avoid using the walrus operator ':='.

Line 22: Use of the walrus operator ':=' detected. Introduced in Python 3.8+.
Suggestion: Refactor to avoid using the walrus operator ':='.

Line 29: Use of positional-only parameters detected. Introduced in Python 3.8+.
Suggestion: Consider refactoring parameters if targeting Python 3.7.

Line 5: Use of f-strings detected. Introduced in Python 3.6, but with enhanced features in Python 3.8+.
Suggestion: Consider refactoring f-strings if targeting an older version of Python.

Line 10: Use of f-strings detected. Introduced in Python 3.6, but with enhanced features in Python 3.8+.
Suggestion: Consider refactoring f-strings if targeting an older version of Python.

Line 23: Use of f-strings detected. Introduced in Python 3.6, but with enhanced features in Python 3.8+.
Suggestion: Consider refactoring f-strings if targeting an older version of Python.

Line 15: Use of structural pattern matching (match-case) detected. Introduced in Python 3.10+.
Suggestion: Refactor to avoid using structural pattern matching.

>>> 


```


## Contributing

* If you want to contribute to the project, please submit a pull request or open an issue to discuss changes or improvements.