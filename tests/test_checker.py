import pytest
from pycompatibility import CompatibilityChecker

@pytest.fixture
def setup_test_file(tmp_path):
    # Define the test file content
    test_file_content = '''\
def example_function():
    x = 10
    y = (z := x + 5)  # Walrus operator (Python 3.8+)
    print(f"The value of z is: {z}")  # f-string (enhanced in Python 3.8+)

    def inner_function(a: int | None):  # Type union operator (Python 3.10+)
        if a is None:
            return "a is None"
        return f"a is {a}"

    result = inner_function(None)
    print(result)

    match result:  # Structural pattern matching (Python 3.10+)
        case "a is None":
            print("Matched None")
        case _:
            print("Matched something else")

    items = [1, 2, 3, 4, 5]
    if any((n := x) > 3 for x in items):  # Walrus operator in comprehensions (Python 3.9+)
        print(f"Found an item greater than 3: {n}")

    context = (open("file1.txt"), open("file2.txt"))  # Parenthesized context managers (Python 3.9+)
    with context as (f1, f2):
        print(f1.read(), f2.read())

    def positional_only_func(a, b, /, c):  # Positional-only parameters (Python 3.8+)
        print(a, b, c)

    positional_only_func(1, 2, 3)

# Calls the example function
example_function()
'''
    # Create a test file with the above content
    test_file = tmp_path / 'test1.py'
    test_file.write_text(test_file_content)
    return test_file

def test_check_compatibility(setup_test_file):
    checker = CompatibilityChecker(setup_test_file)
    issues = checker.verify()

    expected_issues = [
        {'line': 6, 'message': "Use of the type union operator '|' detected. Introduced in Python 3.10+.", 'suggestion': "Replace 'int | None' with 'Optional[int]' from the 'typing' module."},
        {'line': 18, 'message': "Use of structural pattern matching (match-case) detected. Introduced in Python 3.10.", 'suggestion': "Refactor to avoid using structural pattern matching."},
        {'line': 25, 'message': "Use of assignment expressions (walrus operator) in comprehensions detected. Introduced in Python 3.9.", 'suggestion': "Refactor to avoid using assignment expressions in comprehensions."},
        {'line': 25, 'message': "Use of the walrus operator ':=' detected. Introduced in Python 3.8.", 'suggestion': "Refactor to avoid using the walrus operator ':='."},
        {'line': 32, 'message': "Use of positional-only parameters detected. Introduced in Python 3.8.", 'suggestion': "Consider refactoring parameters if targeting Python 3.7."},
        {'line': 15, 'message': "Use of f-strings detected. Introduced in Python 3.6, but with enhanced features in Python 3.8+.", 'suggestion': "Consider refactoring f-strings if targeting an older version of Python."},
        {'line': 25, 'message': "Use of the walrus operator ':=' detected. Introduced in Python 3.8.", 'suggestion': "Refactor to avoid using the walrus operator ':='."},
        {'line': 29, 'message': "Use of assignment expressions (walrus operator) in comprehensions detected. Introduced in Python 3.9.", 'suggestion': "Refactor to avoid using assignment expressions in comprehensions."}
    ]

    assert len(issues) == len(expected_issues)
    for expected, issue in zip(expected_issues, issues):
        assert expected['line'] == issue['line']
        assert expected['message'] == issue['message']
        assert expected['suggestion'] == issue['suggestion']
