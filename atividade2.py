#coding: utf-8

placa = raw_input()

placa1 = placa.split()
              #0,1,2
for i in range(len(placa1)):
	placa2 = placa1[i]
	if placa2[-1] == '1'or placa2[-1] == '2':
		print placa2+':', 'janeiro'
	elif placa2[-1] == '3'or placa2[-1] == '4':
		print placa2+':','fevereiro'
	elif placa2[-1] == '5':
		print placa2+':','março'
	elif placa2[-1] == '6':
		print placa2+':','abril'
	elif placa2[-1] == '7':
		print placa2+':','maio'
	elif placa2[-1] == '8':
		print placa2+':','junho'
	elif placa2[-1] == '9':
		print placa2+':','julho'
	else:
		print placa2+':','agosto'


