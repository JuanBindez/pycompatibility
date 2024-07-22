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

        # Debugging information for the AST code
        #print("AST structure:")
        for node in ast.walk(tree):
            pass
            #print(ast.dump(node, annotate_fields=True))

        # Check type annotations using the type union operator '|'
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

        # Check for walrus operator (Python 3.8+)
        for node in ast.walk(tree):
            if isinstance(node, ast.NamedExpr):
                issues.append({
                    'line': node.lineno,
                    'message': "Use of the walrus operator ':=' detected. Introduced in Python 3.8+.",
                    'suggestion': "Refactor to avoid using the walrus operator ':='."
                })

        # Check for positional-only parameters (Python 3.8+)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if node.args.posonlyargs:
                    issues.append({
                        'line': node.lineno,
                        'message': "Use of positional-only parameters detected. Introduced in Python 3.8+.",
                        'suggestion': "Consider refactoring parameters if targeting Python 3.7."
                    })

        # Check for f-strings expressions (Python 3.8+)
        for node in ast.walk(tree):
            if isinstance(node, ast.FormattedValue):
                issues.append({
                    'line': node.lineno,
                    'message': "Use of f-strings detected. Introduced in Python 3.6, but with enhanced features in Python 3.8+.",
                    'suggestion': "Consider refactoring f-strings if targeting an older version of Python."
                })

        # Check for structural pattern matching (Python 3.10+)
        for node in ast.walk(tree):
            if isinstance(node, ast.Match):
                issues.append({
                    'line': node.lineno,
                    'message': "Use of structural pattern matching (match-case) detected. Introduced in Python 3.10+.",
                    'suggestion': "Refactor to avoid using structural pattern matching."
                })

        return issues

    def verify(self):
        issues = self.check_compatibility()
        for issue in issues:
            print(f"Line {issue['line']}: {issue['message']}")
            print(f"Suggestion: {issue['suggestion']}\n")
