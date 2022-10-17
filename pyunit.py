import unittest
from calculadora import Calculadora

class TesteCalculadora(unittest.TestCase):
    
    def teste_soma(self):
        self.assertEqual(Calculadora.soma(10, 3), 13)
        #Exemplo de erro
        #self.assertEqual(Calculadora.soma(10, 3), 12)
    
    def teste_subtracao(self):
        self.assertEqual(Calculadora.subtracao(10, 3), 7)
        #Exemplo de erro
        #self.assertEqual(Calculadora.subtracao(10, 3), 6)
    
    def teste_multiplicacao(self):
        self.assertEqual(Calculadora.multiplicacao(10, 3), 30)
        #Exemplo de erro
        #self.assertEqual(Calculadora.multiplicacao(10, 0), 10)
    def teste_divisao(self):
        self.assertEqual(Calculadora.divisao(10, 2), 5)
        #Exemplo de erro 1
        #self.assertEqual(Calculadora.divisao(10, 3), 4)
        #Exemplo de erro 2
        #self.assertEqual(Calculadora.divisao(10, 0), 1)
    
if __name__ == '__main__':
    unittest.main()