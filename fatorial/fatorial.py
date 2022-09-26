# coding: utf-8

numero = int(raw_input())
valor = 1
potencia = 1
for i in range(numero):
	valor *= potencia
	if potencia < numero:
		potencia+=1
print valor
