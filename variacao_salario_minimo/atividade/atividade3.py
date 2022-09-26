# coding: utf-8


numero = raw_input()
count = 0
cont = 0
for i in range(len(numero)):
    if i+1 <= len(numero):
        if (int(numero[i]))%2 == 0 and (int(numero[i+1]))%2 != 0:
            count+=1
        
        elif (int(numero[i]))%2 != 0 and (int(numero[i+1]))%2 == 0:
            count+=1
        else:
            count -=1
        cont+=1

print count
print cont
if count == len(numero):
    print "Verdadeiro"+":", len(numero)
else:
    print "Falso"+":", len(numero)
