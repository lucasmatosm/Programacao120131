#coding: utf-8


ano_inicial = int(raw_input())
ano_final = int (raw_input())
ano = -1
valor_real = []
valor_dollar = []
variacao_dollar = []
for i in range(ano_inicial, ano_final + 1):
      valor_real.append(float(raw_input()))
      valor_dollar.append(float(raw_input()))

for i in range(ano_inicial, ano_final + 1):
      ano+= 1 
      variacao_dollar.append(float(valor_real[ano])/float(valor_dollar[ano]))
      if ano  <= 0:
            print str(i)+": R$%.2f = U$%.2f" %(float(valor_real[ano]), float(valor_real[ano])/float(valor_dollar[ano]))
      else:
         
            varia_dollar  = ((float(variacao_dollar[ano]) - float(variacao_dollar[ano-1]))/ float(variacao_dollar[ano-1]))*100
            
            variacao_real = ((float(valor_real[ano]) - float(valor_real[ano-1]))/ float(valor_real[ano-1]))*100

            print str(i)+": R$%.2f = U$%.2f (var: %.2f%% em R$ = %.2f%% em U$)" %(float(valor_real[ano]),(float(valor_real[ano])/float(valor_dollar[ano])) , variacao_real, varia_dollar) 


print "Variação no  período: %.2f%% em R$ = em U$ " %(((float(valor_real[-1]) - float(valor_real[0]))/float(valor_real[0])*100)) 

#((float(variacao_dollar[-1]) -  float (variacao_dollar[0]))/float(variacao_dollar[0])*100)

            
      
      
      
