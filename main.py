# main.py
from pycompatibility import CompatibilityChecker

checker = CompatibilityChecker("example_code.py", python_version="3.11")
checker.verify()