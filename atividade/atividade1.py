#coding: utf-8

x = int(raw_input())
y = int(raw_input())

if x <= y:
    for i in range(x, y+1):
        print i, i**2


else:
    print "---"
