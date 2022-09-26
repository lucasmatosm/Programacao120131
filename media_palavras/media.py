# coding: utf-8

media = 0.0
soma= 1.0
while True:
	palavra = raw_input()
	if palavra == "fim":
		print "%.1f" %(media/soma)
		break
	elif media == 0.0:
		media +=  (len(palavra))
	else :
		soma += 1.0
		media = (media+ len(palavra))
	
		
	
