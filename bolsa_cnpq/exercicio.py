# coding: utf-8

bolsa = 500.0
meses = ['jan', 'fev','mar', 'abr','mai', 'jun' , 'jul','ago', 'set', 'out', 'nov', 'dez']
saldo = 0
saldo_positivo = 0
mes = ""
gastos = raw_input().split()
for i in range(len(meses)):
	saldo = bolsa - int(gastos[i])
	bolsa = saldo + 500 
	if saldo >= saldo_positivo:
		saldo_positivo = saldo
		mes = meses[i]
		
print mes
