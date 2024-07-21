# test_code.py

from typing import Optional

# Example with type union operator (Python 3.10+)
def example_function(param: str | None):
    if param is not None:
        print(param)

# Example with walrus operator (Python 3.8+)
def example_walrus_operator():
    if (n := 10) > 5:
        print(n)

# Example with positional-only parameters (Python 3.8+)
def example_positional_only(a, b, /, c, d):
    print(a, b, c, d)

# Example with f-strings expressions (Python 3.8+)
def example_fstring(name):
    age = 30
    print(f"Name: {name}, Age: {age}")

# Example with zoneinfo module (Python 3.9+)
from zoneinfo import ZoneInfo
def example_zoneinfo():
    tz = ZoneInfo("America/New_York")
    print(tz)
