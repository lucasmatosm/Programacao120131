import unittest
import sys

from undertest import remove_menores

class Testes(unittest.TestCase):

    def test_exemplo(self):
        lista = [1, 2, 3, 4, 5]
        assert remove_menores(3, lista) == 2
        assert lista == [3, 4, 5]

if __name__ == '__main__':
    unittest.main()
