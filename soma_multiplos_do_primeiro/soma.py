#coding: utf-8
#Lucas Matos/ 113111435
#UFCG, 2013.1

numero = int(raw_input())
contador = 0 

for i in range(10):
     valor  = int(raw_input())
     if valor  % numero == 0:
           contador += valor

print contador
