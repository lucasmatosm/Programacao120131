# coding: utf-8
# Lucas Matos
p1 = [3, 4, -5]
p2 = [5, 0, 0, 0, 2, 0, -1]
def soma_polinomios(p1, p2):
	maior, menor = p1, p2
	if len(p1) < len(p2):
		maior, menor = p2, p1
	n = [0] * len(maior)
	
	for i in range(-1, -len(menor)-1, -1):
		n[i] = menor[i] + maior[i]
	for i in range(len(maior) - len(menor)):
		n[i] = maior[i]
	return n
	
print soma_polinomios(p1, p2)
