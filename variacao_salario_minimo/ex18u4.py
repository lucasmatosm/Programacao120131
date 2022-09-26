# coding: utf-8
# Lucas Gama / Programação 1
# variacao_salario_minimo


ano_inicial = int(raw_input())
ano_final = int(raw_input())

# Calculo do salário mínimo no primeiro ano:

salario_inicial = float(raw_input())
cotacao_inicial = float(raw_input())
salario_inicial_dolar = salario_inicial / cotacao_inicial

# Calculo do salário mínimo nos anos seguintes:

salario = []
cotacao = []
salario_dolar = []
salario_anterior = [salario_inicial]
salario_anterior_dolar = [salario_inicial_dolar]
variacao_real = []
variacao_dolar = []
x = 0


for i in range(ano_inicial + 1,ano_final + 1):

    salario.append(float(raw_input()))
    cotacao.append(float(raw_input()))
    salario_dolar.append(salario[x] / cotacao[x])
    variacao_real.append(((salario[x] - salario_anterior[x]) / salario_anterior[x]) * 100.0)
    variacao_dolar.append(((salario_dolar[x] - salario_anterior_dolar[x]) / salario_anterior_dolar[x]) * 100.0)
    salario_anterior.append(salario[x])
    salario_anterior_dolar.append(salario_dolar[x])
    x += 1

# Calculo da variação no período:

variacao_periodo = ((salario[x-1] - salario_inicial) / salario_inicial) * 100.0
variacao_periodo_dolar = ((salario_dolar[x-1] - salario_inicial_dolar) / salario_inicial_dolar) * 100.0

print "%d: R$%.2f = U$%.2f" % (ano_inicial, salario_inicial, salario_inicial_dolar)

y = 0
for i in range(ano_inicial + 1,ano_final + 1):

    print "%d: R$%.2f = U$%.2f (var: %.2f%% em R$ = %.2f%% em U$)" % (i, salario[y], salario_dolar[y], variacao_real[y], variacao_dolar[y])
    y += 1


print "Variação no período: %.2f%% em R$ = %.2f%% em U$" % (variacao_periodo, variacao_periodo_dolar)

