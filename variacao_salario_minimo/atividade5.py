# coding: utf-8

num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())


for i in range(1,num3+1):
    if i%num1 == 0 and i%num2 == 0:
        print i
