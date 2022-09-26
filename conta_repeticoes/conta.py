# coding: utf-8

repeticoes = int(raw_input())
anterior = int(raw_input())
contador = 1

for i in range(1, repeticoes):
	numero = int(raw_input())

for i in range(repeticoes):
	if numero == anterior:
		contador += 1
	else:
		print "%d: %d" %(anterior, contador)
		anterior = numero
		contador = 1
