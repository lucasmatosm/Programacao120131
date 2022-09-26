# coding: utf-8
# Lucas Matos

notamenor = 0.0
notamaior = 10.0
soma = 0
for i in range(5):
    nota = float(raw_input())
    if notamenor < nota:
        notamenor = nota
    if notamaior > nota:
        notamaior = nota
