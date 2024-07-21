# main.py
from pycompatibility import CompatibilityChecker

checker = CompatibilityChecker("script1.py")
checker.report_issues()