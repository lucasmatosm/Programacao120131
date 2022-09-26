import unittest
import sys

from undertest import juncao_ordenada

class Testes(unittest.TestCase):

   def test_1_base(self):
     l1 = [8, 11, 78, 79, 511]
     l2 = [7, 8, 121, 302]
     assert juncao_ordenada(l1, l2) == [7, 8, 8, 11, 78, 79, 121, 302, 511]
     assert l1 == [8, 11, 78, 79, 511]
     assert l2 == [7, 8, 121, 302]

if __name__ == '__main__':
    unittest.main()
