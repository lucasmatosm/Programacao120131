#coding: utf-8
ano = int(raw_input())
if ano%400==0 or ano%4==0 and ano%100 != 0:
    print ano, "é bissexto"
else:
     print ano, "não é bissexto"
