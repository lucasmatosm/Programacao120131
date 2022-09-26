numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())

if numero1 + numero2 + numero3 == 13:
   print "0"
elif numero3 ==13 and numero1 + numero2 != 13:
   num = numero1 + numero2
   print num
elif numero1 != 13 and numero2 != 13 and numero3 != 13:
   num1 = numero1+ numero2 + numero3
   print num1
else:
   print "0"
