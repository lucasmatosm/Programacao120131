#coding: utf-8
#Jessika Renally


#entrada
n = int(raw_input())
numeros = []
ocorrencias = []

#processamento do dados
for i in range(n):
	numero = int(raw_input())
	
	if numero not in numeros:
		numeros.append(numero)
		ocorrencias.append(1)
	else:
		posicao = numeros.index(numero)
		ocorrencias[posicao] += 1
		
#saida
for i in range(len(numeros)):
	print "%d: %d" % (numeros[i], ocorrencias[i])


