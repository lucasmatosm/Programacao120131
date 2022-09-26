# coding: utf-8
# Lucas Matos

soma = 0.0
contador = 0.0
media = 0.0

while True:
    numero = float(raw_input("valor? "))
    if numero < 0.0: break 
    soma += numero
    contador += 1

if contador > 0.0:
    media = soma / contador
print "---"
print "Quantidade de valores: %.f" %contador
print "Soma dos valores: %.1f" %soma
print "Média: %.1f" %media
