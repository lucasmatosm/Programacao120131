# coding utf-8
numero = raw_input()
digito = int(numero[0:2])
digito1 = int (numero[3:5])
soma = digito + digito1
digito2 = int(numero[-3])

multiplica = soma*digito2
print "%04d" %multiplica
