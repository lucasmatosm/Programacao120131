# coding: utf-8
# Lucas Matos

def juncao_ordenada(lista1,lista2):
	l3 = lista1 + lista2
	l4 = []
	while not l3 == []:
		menor = l3[0]
		for i in l3:
			if i < menor:
				menor = i
		l4.append(menor)
		l3.remove(menor)
	return l4


