# coding: utf-8

cadeia_menor = raw_input().split()
cadeia_maior = raw_input().split()

# função para checar se a cadeia_maior é maior que a outra, 
# e se seu tamanho é multiplo de 4
def checa_cadeias(cadeia_menor, cadeia_maior):
    regulador = False
    if len(cadeia_maior) > len(cadeia_menor):
        regulador = True
        if len(cadeia_maior)%4 != 0 or len(cadeia_menor)%4 != 0:
            regulador = False
    return regulador

# execução do programa
if checa_cadeias(cadeia_menor, cadeia_maior): # (retorna True ou False)
    lista = []
    for i in range(len(cadeia_maior)):
        regulador = False
        if cadeia_maior[i] == cadeia_menor[0]:
            j = 0
            for x in range(i, len(cadeia_menor) + i):
                if cadeia_maior[x] == cadeia_menor[j]:
                    regulador = True
                    j += 1
                else:
                    regulador = False
                    break
            if regulador == True:
                lista.append(i+1)
    for e in lista:
        print e
    print e
