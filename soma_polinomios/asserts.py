import unittest
import sys

from undertest import soma_polinomios

class Testes(unittest.TestCase):

    def test_exemplo(self):
        p1 = [3, 4, -5]
        p2 = [5, 0, 0, 0, 2, 0, -1]
        assert soma_polinomios(p1, p2) == [5, 0, 0, 0, 5, 4, -6]

if __name__ == '__main__':
    unittest.main()
