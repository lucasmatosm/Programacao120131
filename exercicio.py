#coding: utf-8

exercicios= raw_input().split()
nomes= raw_input().split()
maior = 0
nome_maior = ""
for i in range(len(nomes)):
	if int(exercicios[i]) > maior:
		maior = int(exercicios[i])
		nome_maior = nomes[i]
print "%s %d" %(nome_maior, maior)
