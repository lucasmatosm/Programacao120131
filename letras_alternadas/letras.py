# coding: utf-8
# Lucas Matos

def letras_alternadas(palavra):
    letras = ""
    for i in range(len(palavra)):
        if i % 2 == 0:
            letras += palavra[i]
    return letras

repeticoes = int(raw_input())
for i in range(repeticoes):
    palavra = raw_input()
    print letras_alternadas(palavra)

        
