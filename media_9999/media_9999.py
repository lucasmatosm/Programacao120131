# coding: utf-8

somador = 0.0
contador = 0.0
media = 0.0

while True:
    numero = raw_input()
    if numero == "9999": break
    somador += float(numero)
    contador += 1

if contador > 0.0:
    media = somador / contador

print "%.1f" %media
    
