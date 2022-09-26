import unittest
import sys

from undertest import indices_de_idosos

class Testes(unittest.TestCase):

   def test_exemplo(self):
        fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
        assert indices_de_idosos(fila) == [2, 3, 9, 10]

if __name__ == '__main__':
    unittest.main()
