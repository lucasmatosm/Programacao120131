# coding: utf-8
# Lucas Matos

def vetor_por_escalar(vetor, escalar):
	multiplica = []
	for i in range(len(vetor)):
		multiplica.append(vetor[i] * escalar)
	return multiplica

