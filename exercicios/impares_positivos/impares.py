#coding: utf-8

numero = int(raw_input())
valor = 1
for i in range(numero):
	if valor < numero and valor%2 != 0:
		print valor
		valor +=2
		
