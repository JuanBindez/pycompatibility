import sys
from pycompatibility import CompatibilityChecker

def main():
    if len(sys.argv) != 2:
        print("Uso: pycompatibility <script.py>")
        sys.exit(1)

    filename = sys.argv[1]
    checker = CompatibilityChecker(filename)
    issues = checker.check_compatibility()

    if issues:
        for issue in issues:
            print(f"Linha {issue['line']}: {issue['message']}")
            print(f"Sugestão: {issue['suggestion']}\n")
    else:
        print("Nenhum problema de compatibilidade detectado.")
