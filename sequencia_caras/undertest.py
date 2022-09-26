# coding: utf-8
# Lucas Matos

def sequecncia_caras(lancamentos):
	contador = 0
	anterior = int(lancamentos[o])
	for i in range(1, len(lancamentos)):
		if lancamentos[i] == anterior:
			if int(lancamentos[i]) == 1:
				contador += 1
			anterior = lancamentos[i]
		else:
			anterior = lancamentos[i]
	return contador

 = raw_input().split()

		
