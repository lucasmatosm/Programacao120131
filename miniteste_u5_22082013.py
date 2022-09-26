#coding: utf-8
#Jessika Renally

#entrada
n = int(raw_input())
numeros = []
for i in range(n):
	numero = float(raw_input())
	numeros.append(numero)

#processamento dos dados
menor_diferenca_abs = abs(abs(numeros[0]) - abs(numeros[1]))
menor_diferenca1 = numeros[0]
menor_diferenca2 = numeros[1]

for i in range(1, n-1):
	if abs(abs(numeros[i]) - abs(numeros[i+1])) < menor_diferenca_abs:
		menor_diferenca_abs = abs(abs(numeros[i]) - abs(numeros[i+1]))
		menor_diferenca1 = numeros[i]
		menor_diferenca2 = numeros[i+1]

#saida
print "%.1f e %.1f" % (menor_diferenca1, menor_diferenca2) 
