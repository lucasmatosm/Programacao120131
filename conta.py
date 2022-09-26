# coding: utf-8

repeticoes = int(raw_input())
anterior = int(raw_input())
contador = 1
numero = []
for i in range(1, repeticoes):
        numero.append(int(raw_input()))

for i in range(len(numero)):
        if numero[i] == anterior:
                contador += 1
        else:
                print "%d: %d" %(anterior, contador)
                anterior = numero[i]
                contador = 1
