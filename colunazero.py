# coding: utf-8
# Lucas Matos
# m = [[5, 0], [3, 1], [2, -4]] == [1]
# m1 = [[1, 3, 0], [0, 1, 0]] == [0, 2]
def colunas_com_zero(m):
    lista = []
    for i in m:
        for j in i:
            if int(j) == 0:
                lista.append(i.index(j))
    ordenada = set(lista)            
    return list(ordenada)
            

print colunas_com_zero([[5, 0], [3, 1], [2, -4]])
print colunas_com_zero([[1, 3, 0], [0, 1, 0]])
