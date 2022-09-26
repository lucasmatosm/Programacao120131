num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())

somatorio = num1 + num2 + num3

if somatorio % 3 == 0:
    print "plif"
elif somatorio % 5 == 0:
    print "plof"
else:
    print "plifplof"
