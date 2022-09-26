# coding: utf-8
# Lucas Matos

contador = 0

while True:
	numero = raw_input().split()
	if int(numero[0])*10 + int(numero[1])*50 == int(numero[2]):
		contador+=1
	else: break 

print contador
