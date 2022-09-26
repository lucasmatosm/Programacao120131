#coding: utf-8

palavra = raw_input()
palavra1 = palavra[0]
count = 0
for i in range(len(palavra)):
	
	if count <= i:
		palavra1 = palavra1 + palavra[count]
		count +=2
print palavra1[1:]
