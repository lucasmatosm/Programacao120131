# coding: utf-8

numero_alunos = int(raw_input())
contador = 0
matricula = []
soma = 0
for i in range(numero_alunos):
	alunos = raw_input().split()
	matricula.append(alunos[0])
	alunos.pop(0)
	if alunos[3] == "-":
		alunos.pop(3)
print alunos
for i in range(len(alunos)):
	soma += float(alunos[i])
	contador += 1
media = soma/contador
if media >= 7.0:
	print "%s %.1f AM" %(matricula[i], media)
elif media <= 4.0:
    print "%s %.1f RM" %(matricula[i], media)
			 
