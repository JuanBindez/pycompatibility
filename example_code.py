# test_code.py

def func(a: list[int]) -> None:
    pass

def another_func(a: int | None) -> None:
    pass

value = [x := 10 for x in range(10)]

def positional_only(a, /, b):
    pass

def f_string_example():
    name = "world"
    greeting = f"Hello, {name}"

match value:
    case []:
        print("Empty list")

def method(self: Self):
    pass

try:
    pass
except* ValueError as e:
    pass


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
    

def process(value: int | str) -> None:
    if isinstance(value, int):
        print(f"Processing integer: {value}")
    else:
        print(f"Processing string: {value}")
