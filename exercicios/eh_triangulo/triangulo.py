# coding: utf-8

lado1 = int(raw_input())
lado2 = int(raw_input())
lado3 = int(raw_input())

if lado1 < (lado2+lado3) and lado1< abs(lado2-lado3):
    print "triangulo valido. %d" %(lado1+lado2+lado3)
elif lado2 < (lado1+lado3) and lado2< abs(lado1-lado3):
    print "triangulo valido. %d" %(lado1+lado2+lado3)
elif lado3 <(lado1+lado2) and lado3 < abs(lado2 - lado1):
    print "triangulo valido. %d" %(lado1+lado2+lado3)
else:
    print "triangulo invalido."

