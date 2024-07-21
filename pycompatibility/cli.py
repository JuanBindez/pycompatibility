import argparse
from pycompatibility import CompatibilityChecker

def main():
    parser = argparse.ArgumentParser(description='Check Python code compatibility.')
    parser.add_argument('filename', type=str, help='The path to the Python file to check.')

    args = parser.parse_args()

    checker = CompatibilityChecker(args.filename)
    
    checker.verify()

if __name__ == '__main__':
    main()
