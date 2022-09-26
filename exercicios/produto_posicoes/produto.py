# coding: utf-8



numero = raw_input()

numero_par = int(numero[1]) + int(numero[-2])
numero_impar = int(numero[0]) + int(numero[2]) + int(numero[-1])

produto = numero_par * numero_impar

print "%0.5d" %produto

