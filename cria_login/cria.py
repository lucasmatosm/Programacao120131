# coding: utf-8:
# LUcas Matos

def cria_login(nome):
	login = str.lower(nome[0])
	for i in range(1, len(nome)):
		if nome[i].lower() != nome[i]:
			login += nome[i][0].lower()
	return login

while True:
	nome = raw_input()
	nomecompleto = nome.split()
	if nomecompleto[0] == "fim": break
	loginlcc = cria_login(nomecompleto)
	print "%s: %s" %(nome, loginlcc)
		
		
		

