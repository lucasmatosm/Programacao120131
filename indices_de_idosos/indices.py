# coding: utf-8
# Lucas Matos

def indices_de_idosos(fila):
	indices = []
	for i in range(len(fila)):
		if fila[i] >= 60:
			indices.append(fila.index(fila[i]))
	return indices

