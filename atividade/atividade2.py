#coding: utf-8

x = int(raw_input())
y = int(raw_input())

if x <= y:
    for i in range(x, y+1):
        g = i**2
        if g %3 == 0:
            print i, g, "*"
        else:
            print i, g


else:
    print "---"
