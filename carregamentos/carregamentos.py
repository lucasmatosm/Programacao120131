# coding: utf-8
#Lucas Matos, UFCG, 2013.1

num_carregamentos = int(raw_input())
variacao = []
maior = 0
mais_demorado = 0
for i in range(num_carregamentos):
	carregamento = raw_input().split()
	variacao.append(int(carregamento[1]) - int(carregamento[0]))

for i in range(num_carregamentos):
	if variacao[i] >=  maior:
		maior = variacao[i]
		mais_demorado = i+1

print "carregamento %d" %mais_demorado
