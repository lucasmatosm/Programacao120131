# coding: utf-8
# Lucas Matos

def determinante(m):
    resultado =  1
    soma = 0
    resultado = m[0][0] * m[1][1] * m[2][2]
    resultado1 = m[0][1] * m[1][2] * m[2][0]
    resultado2 = m[0][2]* m[1][0] * m[2][1]
    resultado3 = m[2][0] * m[1][1] * m[0][2]* -1
    resultado4 = m[2][1] * m[1][2] * m[0][0] * -1
    resultado5 = m[2][2] * m[1][0] * m[0][1] * -1
    soma =  resultado + resultado1 + resultado2 + resultado3 + resultado4 + resultado5
    return soma
m = [[3, 2, 4], [0, 1, 0], [-1, 0, -1]]
m1 = [[1,2,3], [4,5,6], [1, 0, 2]]
print determinante(m)
print determinante(m1)
    
    

