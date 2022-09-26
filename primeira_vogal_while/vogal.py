# coding: utf-8
# Lucas Matos

vogal = "AEIOUaeiou"
contador = 0
while True:
    palavra = raw_input()
    if palavra == "fim": break 
    for e in palavra:
        if e in vogal:
            print e
            break
        else:
            contador += 1
if contador != len(palavra):
    print "-"
    
print contador
print len(palavra)
