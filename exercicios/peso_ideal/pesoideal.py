# coding: utf-8

sexo = raw_input()
altura = float(raw_input())
if sexo == 'm':
    peso = 72.7 * altura - 58
    print "%.3f" %peso
else:
    peso = 62.1 * altura - 44.7
    print "%.3f" %peso
   
