# coding: utf-8
# Lucas Matos

def remove_menores(N, lista):
    contador = 0
    lista1 = []
    for i in range(len(lista)):
        lista1.append(lista[i])
    for i in range(len(lista)):
        if int(lista[i]) < N:
            lista1.remove(lista[i])
            contador +=1
    lista = lista1
    return contador

