#coding: utf-8
valor1 = []
valor2 = []
valor3 = []
meses = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"] 
for i in range(12):
	valor = raw_input()
	valo4 = valor.split()
	valor1.append(valo4[0])
	valor2.append(valo4[-1])
	valor3.append(float(valor1[i]) - float(valor2[i]))

for i in range(12):
	if float(valor3[i]) >0:
		print meses[i], " "+str(valor3[i])
	else:
		print meses[i], valor3[i]
