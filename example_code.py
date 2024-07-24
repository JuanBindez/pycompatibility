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
