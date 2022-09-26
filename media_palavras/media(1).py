# coding: utf-8
# Lucas Matos

soma = 0.0
contador = 0
media = 0.0
while True:
    palavra = raw_input()
    if palavra == "fim": break
    soma += float(len(palavra))
    contador += 1
if contador > 0:
    media = soma / contador

print "%.1f" %media
    
    
