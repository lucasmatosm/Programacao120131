# coding: utf-8
# Lucas Matos

vogal = "AEIOUaeiou"
contador = 0

while True:
    palavra = raw_input()
    if palavra == "***": break
    elif palavra[0] not in vogal:
        contador += 1
print "Palavras: %d" %contador
