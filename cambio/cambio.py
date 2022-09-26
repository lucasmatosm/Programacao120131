# coding: utf-8
# Lucas Matos

conversor = 0

while True:
	valor = raw_input().split()
	if valor[0] == "fim": break
	elif valor[3] == "$":
		conversor = float(valor[1])*2.58
		print "R$ %s = $ %.2f" %(valor[1], conversor)
	elif valor[3] == "€":
		conversor = float(valor[1])*0.38
		print "R$ %s = € %.2f" %(valor[1], conversor)
	else:
		conversor = float(valor[1])*0.49
		print "R$ %s = U$ %.2f" %(valor[1], conversor)
		
