# coding: utf-8
# joao motorista
# Lucas Matos

hodometro_inicio = int(raw_input())
hodometro_fim = int(raw_input())
combustivel = int(raw_input())
valor = float(raw_input())

consumo = int((hodometro_fim  - hodometro_inicio)/combustivel)
lucro = valor -   (combustivel*2.55) 

print  "Consumo em Km/L: %d" %consumo
print "Lucro liquido: %.2f" %lucro
