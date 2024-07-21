import ast

class CompatibilityChecker:
    def __init__(self, filename):
        self.filename = filename
        self.python_version = "3.7"

    def check_compatibility(self):
        with open(self.filename, "r") as file:
            source_code = file.read()

        tree = ast.parse(source_code)
        issues = []

        # Add debugging information for the AST code
        print("AST structure:")
        for node in ast.walk(tree):
            # Uncomment the next line to see the full AST structure
            # print(ast.dump(node, annotate_fields=True))
            pass

        # Check type annotations
        for node in ast.walk(tree):
            if isinstance(node, ast.AnnAssign):
                annotation = node.annotation
                if isinstance(annotation, ast.BinOp) and isinstance(annotation.op, ast.BitOr):
                    left = annotation.left
                    right = annotation.right
                    if isinstance(left, ast.Name) and isinstance(right, ast.Constant) and right.value is None:
                        if left.id == 'str':
                            issues.append({
                                'line': node.lineno,
                                'message': "Use of the type union operator '|' detected. Introduced in Python 3.10.",
                                'suggestion': "Replace 'str | None' with 'Optional[str]' from the 'typing' module."
                            })

            elif isinstance(node, ast.FunctionDef):
                for arg in node.args.args:
                    if isinstance(arg.annotation, ast.BinOp) and isinstance(arg.annotation.op, ast.BitOr):
                        left = arg.annotation.left
                        right = arg.annotation.right
                        if isinstance(left, ast.Name) and isinstance(right, ast.Constant) and right.value is None:
                            if left.id == 'str':
                                issues.append({
                                    'line': arg.lineno,
                                    'message': "Use of the type union operator '|' detected. Introduced in Python 3.10.",
                                    'suggestion': "Replace 'str | None' with 'Optional[str]' from the 'typing' module."
                                })

        # Check for walrus operator (Python 3.8+)
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.BinOp) and isinstance(node.value.op, ast.Assign):
                issues.append({
                    'line': node.lineno,
                    'message': "Use of the walrus operator ':=' detected. Introduced in Python 3.8.",
                    'suggestion': "Refactor to avoid using the walrus operator ':='."
                })

        # Check for positional-only parameters (Python 3.8+)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if node.args.posonlyargs:
                    issues.append({
                        'line': node.lineno,
                        'message': "Use of positional-only parameters detected. Introduced in Python 3.8.",
                        'suggestion': "Consider refactoring parameters if targeting Python 3.7."
                    })

        # Check for f-strings expressions (Python 3.8+)
        for node in ast.walk(tree):
            if isinstance(node, ast.FormattedValue):  # Corrected attribute name
                issues.append({
                    'line': node.lineno,
                    'message': "Use of f-strings detected. Introduced in Python 3.6, but with enhanced features in Python 3.8+.",
                    'suggestion': "Consider refactoring f-strings if targeting an older version of Python."
                })

        return issues

    def verify(self):
        issues = self.check_compatibility()
        for issue in issues:
            print(f"Line {issue['line']}: {issue['message']}")
            print(f"Suggestion: {issue['suggestion']}\n")
