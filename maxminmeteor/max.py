# coding: utf-8

valores = raw_input().split()
tempo = raw_input().split()
variavel_fisica = []
minimo = 1000.0
maximo = 0.0
tempo_maximo = ""
tempo_menimo = ""
for i in range(len(valores)):
	variavel_fisica.append(float(valores[i]))
	
for i in range(len(valores)):
	if variavel_fisica[i] > maximo:
		maximo = variavel_fisica[i]
		tempo_maximo = tempo[i]
	elif variavel_fisica[i] < minimo:
		minimo = variavel_fisica[i]
		tempo_minimo = tempo[i]
		
print "Min: %s %.2f" %(tempo_minimo, minimo) 
print "Max: %s %.2f" %(tempo_maximo, maximo) 
		

	
