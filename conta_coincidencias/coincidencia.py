# coding: utf-8
# Lucas Matos


def conta_coincidencias(lista1, lista2):
	contador = 0
	if len(lista1) > len(lista2):
		for  i in range(len(lista2)):
			if lista1[i] == lista2[i]:
				contador += 1 
	elif len(lista1) < len(lista2):
		for  i in range(len(lista1)):
			if lista1[i] == lista2[i]:
				contador += 1
	else:
		for  i in range(len(lista1)):
			if lista1[i] == lista2[i]:
				contador += 1
	return contador


lista1 = raw_input().split()
lista2 = raw_input().split()

print conta_coincidencias(lista1, lista2)

assert conta_coincidencias([1,2,3,4], [5,6,7]) == 0
assert conta_coincidencias([1,2,3,4], [2,3,3,4]) == 2
assert conta_coincidencias([1,2],[1,3]) == 1
