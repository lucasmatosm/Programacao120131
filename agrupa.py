# coding: utf-8
# Lucas Matos

def agrupa_pares_impares(lista):
    dici = {}
    pares =[]
    impares =[]
    for i in range(len(lista)):
        if int(lista[i]) % 2 == 0:
            pares.append(int(lista[i]))
        else:
            impares.append(int(lista[i]))
    dici["impares"] = impares
    dici["pares"] = pares
    return dici
    
numeros = raw_input().split()
print agrupa_pares_impares(numeros)
            
