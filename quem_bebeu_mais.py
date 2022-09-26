# coding: utf-8
# Lucas Matos

def quem_bebeu_mais(m):
    amigo1, amigo2, amigo3 = 0, 0, 0
    bebidas = []
    bebeu_mais = 0
    for j in range(len(m[0])):
        for i in range(len(m)):
            if j == 0:
                amigo1 += m[i][j]
            elif j == 1:
                 amigo2 += m[i][j]
            else:
                 amigo3 += m[i][j]
    bebidas.append(amigo1)
    bebidas.append(amigo2)
    bebidas.append(amigo3)
    for i in range(len(bebidas)):
        if bebeu_mais < bebidas[i]:
            bebeu_mais = bebidas[i]
    return (bebidas.index(bebeu_mais) +1)

print quem_bebeu_mais([[1,2,3], [0,1,0], [3,1,2]])
            
            
