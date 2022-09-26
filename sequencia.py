# coding: utf-8
# Lucas Matos

numero = 1
valor = numero + numero**2
sentinela = int(raw_input())
print valor
while True:
	if valor < sentinela:
		valor = valor*2
	elif valor > sentinela: break 
	print valor
	

