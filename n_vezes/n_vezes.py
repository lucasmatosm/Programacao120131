# coding: utf-8
# Lucas Matos

while True:
	numeros = raw_input().split()
	if float(numeros[0]) < 0.0 and float(numeros[1]) < 0.0: break 
	print "%.1f" %(float(numeros[0])*float(numeros[1]))
