# coding: utf-8
# Lucas Matos

import math

def areaQuadrado(lado):
	return lado**2 
def areaTriangulo(base, altura):
	return (base*altura) / 2.0 
def areaCirculo(raio):
	return math.pi * raio**2
	
while True:
	calcula = raw_input().split()
	if calcula[0] == "fim": break
	elif calcula[0] == "Q":
		quadrado = areaQuadrado(float(calcula[1]))
		print "A área do quadrado é %.2f" %(quadrado)
	elif calcula[0] == "C":
		circulo = areaCirculo(float(calcula[1]))
		print "A área do círculo é %.2f" %(circulo)
	else:
		triangulo  = areaTriangulo(float(calcula[1]), float(calcula[2]))
		print "A área do triangulo é %.2f" %(triangulo)
		
