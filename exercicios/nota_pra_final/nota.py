nota_parcial = float(raw_input())
if nota_parcial < 4.0:
    print "Reprovado"
elif 4.0 <= nota_parcial <= 7.0:
     nota = (5.0 - (nota_parcial*0.6))/0.4
     print nota
else:
     print "Aprovado"
