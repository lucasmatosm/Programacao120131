# coding: utf-8
# Lucas Matos

def remove_palavras_com_menos_vogais(lista):
	vogais = "AEIOUaeiou"
	cont_vogais = 0
	cont_consoantes = 0
	j = 0
	for i in range(len(lista)):
		for e in lista[j]:
			if e in vogais:
				cont_vogais += 1
			else:
				cont_consoantes +=1
		if cont_vogais < cont_consoantes:
			lista.pop(j)
		else:
			j += 1
	return lista 

print remove_palavras_com_menos_vogais(['arara', 'tv',   'bacia'])
	
	
