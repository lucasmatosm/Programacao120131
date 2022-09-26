# coding: utf-8
# Lucas Matos

soma_pares, soma_impares = 0, 0
cont_pares, cont_impares, cont_geral = 0, 0, 0
media_pares, media_impares = 0.0, 0.0
media_geral, soma_geral = 0.0, 0

while True:
	numero = int(raw_input())
	if numero == 0: break
	elif numero %2 == 0:
		soma_pares += numero
		cont_pares += 1
	elif numero %2 != 0:
		soma_impares += numero
		cont_impares += 1
	soma_geral += numero
	cont_geral += 1

if cont_pares != 0:
	media_pares =  float(soma_pares)/ float(cont_pares)  
if cont_impares != 0:
	media_impares =  float(soma_impares)/ float(cont_impares)
if cont_geral != 0:
	media_geral =  float(soma_geral)/ float(cont_geral)
	
print "pares: %d" %cont_pares
print "impares: %d" %cont_impares
print "media pares: %.1f" %media_pares
print "media impares: %.1f" %media_impares
print "media geral: %.1f" %media_geral
	
	
		
	
