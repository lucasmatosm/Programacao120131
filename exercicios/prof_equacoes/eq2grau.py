a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

delta = (b**2) - (4*a*c)
import math
if delta > 0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print "x1 = %.2f" %x1
    print "x2 = %.2f" %x2
elif delta <0:
    print "sem raizes reais"

else:
    x = (-b + math.sqrt(delta))/(2*a)
    print "x = %.2f" %x
