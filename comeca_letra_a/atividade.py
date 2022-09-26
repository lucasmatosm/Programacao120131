# coding: utf-8

contador = 0

while True:
	palavra = raw_input()
	if palavra[0] == "A":
		print "..."
		print "%d %s" %(contador, palavra)
		break
	else:
		contador += 1
