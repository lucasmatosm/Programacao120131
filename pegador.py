#coding: utf-8

n1= int(raw_input())
horas = []
maior = 0
inicial = raw_input().split()
hora_inicial = int(inicial[0])
horas.append(int(inicial[1]) - int(inicial[0]))
contador = horas[0]

for i in range(n1-1):
	dif_horas = raw_input().split()
	horas.append(int(dif_horas[1]) - int(dif_horas[0])) 
for i in range(1, n1):
	contador += horas[i]
	
for i in range(n1-1):
	if horas[i] > maior:
		maior = horas[i]
total_horas = int(dif_horas[1]) - hora_inicial
sem_pegar = total_horas - contador

print "%d horas durou a maior pegada" %maior
print "%d horas sem pegar ninguem" %sem_pegar


