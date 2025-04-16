import unittest
from src.exceptions import ingrese_numero
from unittest.mock import patch

class TestIngresoNumeroValido(unittest.TestCase):

    @patch('builtins.input', return_value='42')
    def test_ingreso_valido(self, mock_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 42)
    
    @patch('builtins.input', return_value='0')
    def test_ingreso_cero(self, mock_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 0)

    @patch('builtins.input', return_value='1000000')
    def test_ingreso_grande(self, mock_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 1000000)

    @patch('builtins.input', return_value=' 10 ')
    def test_ingreso_con_espacios(self, mock_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 10)

if __name__ == '__main__':
    unittest.main()