# coding: utf-8
# Lucas Matos

def agrupa_negativos(lista):
	agrupa = {}
	negativos, positivos = [], [] 
	for i in range(len(lista)):
		if int(lista[i]) < 0:
			negativos.append(int(lista[i]))
		else:
			positivos.append(int(lista[i]))
	agrupa["nao-negativos"] = positivos
	agrupa["negativos"] = negativos
	return agrupa

	
			
			
