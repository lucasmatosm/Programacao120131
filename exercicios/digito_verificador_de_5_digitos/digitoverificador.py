numero = raw_input()
codigo1 = numero[0]
codigo2 = numero[1]
codigo3 = numero[2]
codigo4 = numero[3]
codigo5 = numero[4]

num1 = int(codigo1)
num2 = int(codigo2)
num3 = int(codigo3)
num4 = int(codigo4)
num5 = int(codigo5)
conta1 = num1+num2+num3+num4+num5

numero_verificador = (num1 + num2 + num3 + num4 + num5)%11
print numero +"-%02.f" %numero_verificador
