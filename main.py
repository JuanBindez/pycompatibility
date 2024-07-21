# main.py
from pycompatibility import CompatibilityChecker

checker = CompatibilityChecker("script2.py")
checker.report_issues()