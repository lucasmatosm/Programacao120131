# coding: utf-8
# Lucas Matos

while True:
    resistores = raw_input().split()
    if (int(resistores[0]) * int(resistores[1])) / (int(resistores[0]) +  int(resistores[1])) == 0:
        print 0
        break 
    else:
        resistencia = (int(resistores[0]) * int(resistores[1])) / (int(resistores[0]) +  int(resistores[1]))
        print resistencia
