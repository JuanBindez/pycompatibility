import unittest
from pycompatibility import CompatibilityChecker

class TestCompatibilityChecker(unittest.TestCase):
    def setUp(self):
        # Cria um arquivo temporário para testes
        self.filename = 'test_script.py'
        with open(self.filename, 'w') as f:
            f.write("""
def example_function(token_file: str | None = None):
    pass

def another_function(value: int | str = 42):
    pass

f_string_example = f"Value is: {value}"
""")

    def test_check_compatibility(self):
        checker = CompatibilityChecker(self.filename)
        issues = checker.check_compatibility()
        
        # Atualize os testes conforme a saída real do CompatibilityChecker
        
        expected_issues = [
            {'line': 2, 'message': "Uso do operador de união de tipos '|' detectado. Introduzido no Python 3.10.",
             'suggestion': "Substitua 'str | None' por 'Optional[str]' do módulo 'typing'."},
            {'line': 4, 'message': "Uso do operador de união de tipos '|' detectado. Introduzido no Python 3.10.",
             'suggestion': "Substitua 'int | str' por 'Union[int, str]' do módulo 'typing'."},
            {'line': 7, 'message': "Uso de f-strings com expressões detectado. Introduzido no Python 3.8.",
             'suggestion': "Substitua f-strings com expressões por f-strings mais simples ou concatenar strings manualmente."}
        ]
        
        # Verifica se todas as questões esperadas estão presentes nos problemas detectados
        for issue in expected_issues:
            self.assertIn(issue, issues)

    def tearDown(self):
        import os
        # Remove o arquivo de teste
        if os.path.exists(self.filename):
            os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()
