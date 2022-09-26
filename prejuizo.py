#coding: utf-8

meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
receita = []
valor1 = raw_input().split()
valor2 = raw_input().split()

for i in range(12):
	receita.append(float(valor1[i])-float(valor2[i]))
	
for i in range(12):
	if receita[i] < 0.0:
		print "%s %.1f" %(meses[i], receita[i])
	
