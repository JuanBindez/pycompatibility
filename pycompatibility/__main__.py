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
            pass
            #print(ast.dump(node, annotate_fields=True))

        # Check type annotations
        for node in ast.walk(tree):
            if isinstance(node, ast.AnnAssign):
                annotation = node.annotation
                # Add annotation text check
                if isinstance(annotation, ast.BinOp) and isinstance(annotation.op, ast.BitOr):
                    left = annotation.left
                    right = annotation.right
                    # Check if the annotation is something like 'str | None'
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

        return issues

    def report_issues(self):
        issues = self.check_compatibility()
        for issue in issues:
            print(f"Line {issue['line']}: {issue['message']}")
            print(f"Suggestion: {issue['suggestion']}\n")
