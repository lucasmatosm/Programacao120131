# coding: utf-8
# hello, world!
# (c) 2013, Lucas Matos/UFCG, programação 1

print "Digite as variaveis a, b e c de uma equação de segundo grau"
a = float(raw_input())
b = float(raw_input())
c = float(raw_input())

delta = b**2 - 4 * a * c
import math
if delta >0:
   x1 = (-b + math.sqrt(delta))/(2 * a)
   x2 = (-b - math.sqrt(delta)) /(2 * a)
   print "As raizes da equação são: %.2f" %x1, "%.2f " %x2
elif delta < 0:
  print "A equação não tem raiz"


else:
   x1 = (-b + math.sqrt(delta)) /(2 * a)
   print "A raiz da equação é:%.2f " %x1


