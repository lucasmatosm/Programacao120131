# coding: utf-8

ni = int(raw_input())
print ni
while True:
	if ni%2 != 0:
		ni = 3*ni +1
		print ni
	else:
		ni = ni/2
		print ni
	if ni == 1: break
		 
