# coding: utf-8

palavra = raw_input()

for i in range(len(palavra)):
	if palavra[i] == 'o' or palavra[i] == 'a' or palavra[i] == 'e' or palavra[i] == 'i' or palavra[i] == 'u':
		print palavra[i]
		break
	
