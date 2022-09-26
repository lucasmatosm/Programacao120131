# coding: utf-8 
# Lucas Matos

def juncao_ordenada(lista1, lista2):
    ordena = []
    lista3 = lista1 + lista2
    print lista3
    menor = int(lista3[0])
    ordena.append(menor)
    print ordena
    for i in range(1, len(lista3)):
        if int(menor) < int(lista3[i]):
            menor = int(lista3[i])
    for i in range(1, len(lista3)):
        if int(menor) > int(lista3[i]):
            ordena.append(lista3[i])
            print ordena
    return ordena

lista1 = raw_input().split()
lista2 = raw_input().split()

print juncao_ordenada(lista1, lista2)
    
 
