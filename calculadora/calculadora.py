# coding: utf-8
# Lucas Matos

def calculadora(numero1, numero2, numero3):
		if numero1 == 1:
			resultado = numero2 + numero3
			return resultado
		elif numero1 == 2:
			resultado = numero2 - numero3
			return resultado
		elif numero1 == 3:
			resultado = numero2 * numero3
			return resultado
		elif numero1 == 4 and numero3 != 0:
			resultado = numero2 / numero3
			return resultado
		else:
			return "Erro: Divisão por 0"
while True:
	calcula = raw_input().split()
	if calcula[0] == "5": break 
	numero1 = int(calcula[0])
	numero2 = int(calcula[1])
	numero3 = int(calcula[2])
	print calculadora(numero1, numero2, numero3)
