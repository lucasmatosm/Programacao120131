# coding: utf-8

numero_paises = int(raw_input())
paises = []
taxa = []
maior = 0
pais = "pais"
for i in range(numero_paises):
	paises.append(raw_input())
for i in range(numero_paises):
	taxa.append(float(raw_input()))
	
	
for i in range(numero_paises):
	if taxa[i]> maior:
		maior = taxa[i]
		pais = paises[i]
		
print "%s: %.1f%%" %(pais, maior)

