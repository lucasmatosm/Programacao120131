# coding: utf-8

sequencia1 = raw_input()
sequencia2 = raw_input()
sequencia3 = raw_input()

quantidade1 = len(sequencia1)
quantidade2 = len(sequencia2)
quantidade3 = len(sequencia3)

if quantidade1< quantidade2 < quantidade3:
    print "%s %d" %(sequencia1, quantidade1)
elif quantidade1<quantidade3<quantidade2:
    print "%s %d" %(sequencia1, quantidade1)
elif quantidade2< quantidade1 < quantidade3:
    print "%s %d" %(sequencia2, quantidade2)
elif quantidade2< quantidade3< quantidade1:
    print "%s %d" %(sequencia2, quantidade2)
elif quantidade3 <quantidade2 <quantidade1:
    print "%s %d" %(sequencia3, quantidade3)
elif quantidade3 <quantidade1<quantidade2:
    print "%s %d" %(sequencia3, quantidade3)
elif quantidade1 == quantidade2:
    print "%s %d" %(sequencia1, quantidade1)
elif quantidade1 == quantidade3:
    print "%s %d" %(sequencia1, quantidade1)
elif quantidade2==quantidade3:
    print "%s %d" %(sequencia2, quantidade2)
    

