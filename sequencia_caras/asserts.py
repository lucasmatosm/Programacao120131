import unittest
import sys

from undertest import sequencia_caras

ae = lambda x, y, z : x.assertEquals(y, z)

class Testes(unittest.TestCase):

    def test_1_exemplo(self):
        jogo1 = [0,1,1,0,1,0,0,0]
        jogo2 = [1,0,1]
        jogo3 = [0,1,1,1,0]

        ae(self, sequencia_caras( jogo1 ), 2)
        ae(self, sequencia_caras( jogo2 ), 1)
        ae(self, sequencia_caras( jogo3 ), 3)

if __name__ == '__main__':
    unittest.main()
