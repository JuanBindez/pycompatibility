
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

    # Example for 'Self' type (Python 3.11+)
    class MyClass:
        def method(self: Self):  # Self type
            print("Using Self type")

    obj = MyClass()
    obj.method()

    # Example for 'except*' clause (Python 3.11+)
    try:
        raise ValueError("An error occurred")
    except *ValueError as e:  # except* clause
        print(f"Caught an exception: {e}")