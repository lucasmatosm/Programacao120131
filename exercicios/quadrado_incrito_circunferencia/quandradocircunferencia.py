# coding: utf-8
import math

lado = float(raw_input())

raio = (lado * math.sqrt(2))/2
perimetro = 2 * raio * math.pi
area = math.pi*(raio**2)

print "Perímetro: %.5f" %perimetro
print "Área: %.5f" %area
