import unittest
from src.exceptions import ingrese_numero
from unittest.mock import patch
from src.exceptions import ingrese_numero, NumeroDebeSerPositivo

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
    @patch('builtins.input', return_value='-1')
    def test_menos_uno(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='-100')
    def test_menos_cien(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='-999999')
    def test_menos_grande(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value=' -5 ')
    def test_con_espacios_negativos(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='AAA')
    def test_entrada_texto(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='!@#')
    def test_entrada_simbolos(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='texto123')
    def test_entrada_mixta(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value=' ')
    def test_entrada_espacio(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main()