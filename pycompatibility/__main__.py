import ast

class CompatibilityChecker:
    """
    A class to check Python code compatibility with a specified Python version.

    Attributes:
        filename (str): The name of the file containing the source code to check.
        python_version (str): The target Python version for compatibility checking.
    """

    def __init__(self, filename, python_version="3.7"):
        """
        Initializes the CompatibilityChecker with the given filename and Python version.

        Parameters:
            filename (str): The name of the file containing the source code to check.
            python_version (str): The target Python version for compatibility checking.
        """
        self.filename = filename
        self.python_version = python_version

    def check_compatibility(self):
        """
        Checks the compatibility of the source code with the specified Python version.

        Parses the source code into an AST (Abstract Syntax Tree) and detects
        various Python version-specific features that might be incompatible with
        the specified version.

        Returns:
            list: A list of issues found, where each issue is represented as a
                  dictionary containing the line number, a message, and a suggestion.
        """
        with open(self.filename, "r") as file:
            source_code = file.read()

        tree = ast.parse(source_code)
        issues = []

        issues.extend(self.check_list_syntax(tree))
        issues.extend(self.check_type_union_operator(tree))
        issues.extend(self.check_walrus_operator(tree))
        issues.extend(self.check_positional_only_parameters(tree))
        issues.extend(self.check_f_strings(tree))
        issues.extend(self.check_structural_pattern_matching(tree))
        issues.extend(self.check_self_type(tree))
        issues.extend(self.check_except_star(tree))

        return issues

    def check_list_syntax(self, tree):
        """
        Checks for the use of list[T] syntax introduced in Python 3.9+.

        Parameters:
            tree (ast.AST): The AST of the source code.

        Returns:
            list: A list of issues related to the use of list[T] syntax.
        """
        issues = []
        if self.version_at_least("3.9"):
            for node in ast.walk(tree):
                if isinstance(node, ast.AnnAssign):
                    if isinstance(node.annotation, ast.Subscript):
                        if isinstance(node.annotation.value, ast.Name) and node.annotation.value.id == 'list':
                            issues.append({
                                'line': node.lineno,
                                'message': "Use of list[T] syntax detected. Introduced in Python 3.9+.",
                                'suggestion': "Replace 'list[T]' with 'List[T]' from the 'typing' module."
                            })
                elif isinstance(node, ast.FunctionDef):
                    for arg in node.args.args:
                        if isinstance(arg.annotation, ast.Subscript):
                            if isinstance(arg.annotation.value, ast.Name) and arg.annotation.value.id == 'list':
                                issues.append({
                                    'line': arg.lineno,
                                    'message': "Use of list[T] syntax detected. Introduced in Python 3.9+.",
                                    'suggestion': "Replace 'list[T]' with 'List[T]' from the 'typing' module."
                                })
        return issues

    def check_type_union_operator(self, tree):
        """
        Checks for the use of the type union operator '|' introduced in Python 3.10+.

        Parameters:
            tree (ast.AST): The AST of the source code.

        Returns:
            list: A list of issues related to the use of the type union operator.
        """
        issues = []
        if self.version_at_least("3.10"):
            for node in ast.walk(tree):
                if isinstance(node, ast.AnnAssign):
                    annotation = node.annotation
                    if isinstance(annotation, ast.BinOp) and isinstance(annotation.op, ast.BitOr):
                        left = annotation.left
                        right = annotation.right
                        if isinstance(left, ast.Name) and isinstance(right, ast.Constant) and right.value is None:
                            issues.append({
                                'line': node.lineno,
                                'message': "Use of the type union operator '|' detected. Introduced in Python 3.10+.",
                                'suggestion': "Replace 'int | None' with 'Optional[int]' from the 'typing' module."
                            })
                elif isinstance(node, ast.FunctionDef):
                    for arg in node.args.args:
                        if isinstance(arg.annotation, ast.BinOp) and isinstance(arg.annotation.op, ast.BitOr):
                            left = arg.annotation.left
                            right = arg.annotation.right
                            if isinstance(left, ast.Name) and isinstance(right, ast.Constant) and right.value is None:
                                issues.append({
                                    'line': arg.lineno,
                                    'message': "Use of the type union operator '|' detected. Introduced in Python 3.10+.",
                                    'suggestion': "Replace 'int | None' with 'Optional[int]' from the 'typing' module."
                                })
        return issues

    def check_walrus_operator(self, tree):
        """
        Checks for the use of the walrus operator ':=' introduced in Python 3.8+.

        Parameters:
            tree (ast.AST): The AST of the source code.

        Returns:
            list: A list of issues related to the use of the walrus operator.
        """
        issues = []
        if self.version_at_least("3.8"):
            for node in ast.walk(tree):
                if isinstance(node, ast.NamedExpr):
                    issues.append({
                        'line': node.lineno,
                        'message': "Use of the walrus operator ':=' detected. Introduced in Python 3.8+.",
                        'suggestion': "Refactor to avoid using the walrus operator ':='."
                    })
        return issues

    def check_positional_only_parameters(self, tree):
        """
        Checks for the use of positional-only parameters introduced in Python 3.8+.

        Parameters:
            tree (ast.AST): The AST of the source code.

        Returns:
            list: A list of issues related to the use of positional-only parameters.
        """
        issues = []
        if self.version_at_least("3.8"):
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if node.args.posonlyargs:
                        issues.append({
                            'line': node.lineno,
                            'message': "Use of positional-only parameters detected. Introduced in Python 3.8+.",
                            'suggestion': "Consider refactoring parameters if targeting Python 3.7."
                        })
        return issues

    def check_f_strings(self, tree):
        """
        Checks for the use of f-strings introduced in Python 3.6, with enhanced features in Python 3.8+.

        Parameters:
            tree (ast.AST): The AST of the source code.

        Returns:
            list: A list of issues related to the use of f-strings.
        """
        issues = []
        if self.version_at_least("3.6"):
            for node in ast.walk(tree):
                if isinstance(node, ast.FormattedValue):
                    issues.append({
                        'line': node.lineno,
                        'message': "Use of f-strings detected. Introduced in Python 3.6, but with enhanced features in Python 3.8+.",
                        'suggestion': "Consider refactoring f-strings if targeting an older version of Python."
                    })
        return issues

    def check_structural_pattern_matching(self, tree):
        """
        Checks for the use of structural pattern matching (match-case) introduced in Python 3.10+.

        Parameters:
            tree (ast.AST): The AST of the source code.

        Returns:
            list: A list of issues related to the use of structural pattern matching.
        """
        issues = []
        if self.version_at_least("3.10"):
            for node in ast.walk(tree):
                if isinstance(node, ast.Match):
                    issues.append({
                        'line': node.lineno,
                        'message': "Use of structural pattern matching (match-case) detected. Introduced in Python 3.10+.",
                        'suggestion': "Refactor to avoid using structural pattern matching."
                    })
        return issues

    def check_self_type(self, tree):
        """
        Checks for the use of the 'Self' type introduced in Python 3.11+.

        Parameters:
            tree (ast.AST): The AST of the source code.

        Returns:
            list: A list of issues related to the use of the 'Self' type.
        """
        issues = []
        if self.version_at_least("3.11"):
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    for arg in node.args.args:
                        if isinstance(arg.annotation, ast.Name) and arg.annotation.id == 'Self':
                            issues.append({
                                'line': arg.lineno,
                                'message': "Use of 'Self' type detected. Introduced in Python 3.11+.",
                                'suggestion': "Replace 'Self' with the current class name."
                            })
        return issues

    def check_except_star(self, tree):
        """
        Checks for the use of the 'except*' clause introduced in Python 3.11+.

        Parameters:
            tree (ast.AST): The AST of the source code.

        Returns:
            list: A list of issues related to the use of the 'except*' clause.
        """
        issues = []
        if self.version_at_least("3.11"):
            for node in ast.walk(tree):
                if isinstance(node, ast.ExceptHandler):
                    if isinstance(node.type, ast.BinOp) and isinstance(node.type.op, ast.BitOr):
                        issues.append({
                            'line': node.lineno,
                            'message': "Use of 'except*' clause detected. Introduced in Python 3.11+.",
                            'suggestion': "Refactor to avoid using 'except*' clause."
                        })
        return issues

    def version_at_least(self, version):
        """
        Compares the current Python version with a specified version.

        Parameters:
            version (str): The version to compare against (e.g., "3.8").

        Returns:
            bool: True if the current version is greater than or equal to the specified version, False otherwise.
        """
        current_version = tuple(map(int, self.python_version.split(".")))
        target_version = tuple(map(int, version.split(".")))
        return current_version >= target_version

    def verify(self):
        """
        Verifies the source code for compatibility issues and prints out the detected issues.

        This method calls the compatibility checking methods and outputs the issues found
        along with suggested fixes.
        """
        issues = self.check_compatibility()
        for issue in issues:
            print(f"Line {issue['line']}: {issue['message']}")
            print(f"Suggestion: {issue['suggestion']}\n")
