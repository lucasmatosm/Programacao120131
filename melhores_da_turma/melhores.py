# coding: utf-8
# Lucas Matos, UFCG, 2013.1

alunos = int(raw_input())
nomes = []
notas_lista = []
maior = 0
segundo_maior = 0
nome_maior = "maior"
nome_segundo = "segundo"
for i in range(alunos):
	nomes.append(raw_input())
	nota = raw_input()
	if nota == "f" or nota == "F":
		notas_lista.append(0.0)
	else:
		notas_lista.append(float(nota))
		
for i in range(alunos):
	if notas_lista[i] > maior:
		maior = notas_lista[i]
		nome_maior = nomes[i]
	elif notas_lista[i] < maior and notas_lista[i]> segundo_maior:
		segundo_maior = notas_lista[i]
		nome_segundo = nomes[i]
		
print "%s, %.1f" %(nome_maior, maior) 
print "%s, %.1f" %(nome_segundo, segundo_maior)

	

	
	
	
