# coding: utf-8
# Lucas Matos

def remove_menores(N, lista):
	contador = 0
	for i in range(len(lista)-1, -1, -1):
		if lista[i] < N:
			lista.remove(lista[i])
			contador += 1
	return contador

