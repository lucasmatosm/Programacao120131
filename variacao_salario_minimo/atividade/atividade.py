# coding utf-8

numero = int(raw_input())
count = 1

for i in range(12):
    if numero%count == 0 and count != numero:
        print count
    count +=1
