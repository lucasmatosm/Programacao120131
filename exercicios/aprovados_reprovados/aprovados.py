# coding: utf-8

numero_alunos = int(raw_input())
soma1 = 0
soma2  = 0
aprovacao = 0
reprovacao = 0
for i in range(numero_alunos):
	nota = float(raw_input())
	if nota >= 7.0:
		soma1 += nota
		aprovacao +=1
	else:
		soma2 += nota
		reprovacao +=1
		
if reprovacao == 0:
	media_aprovados = soma1/aprovacao
	print "Reprovados: 0\n"
	print "Aprovados: %d" %aprovacao
	print "Média: %.1f" %media_aprovados

elif aprovacao == 0:
	media_reprovados = soma2/reprovacao
        print "Reprovados: %d\n" %reprovacao
	print "Média: %.1f" %media_reprovados
	print "Aprovados: 0"
	
	
else:
	media_reprovados = soma2/reprovacao
	media_aprovados = soma1/aprovacao
	print "Reprovados: %d" %reprovacao
	print "Média: %.1f\n" %media_reprovados
        print "Aprovados: %d" %aprovacao
	print "Média: %.1f" %media_aprovados
	
	
