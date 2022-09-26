#coding:utf-8
# Lucas matos

def tem123(lista):
    tem = [1,2,3]
    lista1 = []
    for i in range(len(lista)):
        regulador = False
        if lista[i] == tem[0]:
            j = 0
            for x in range(i, len(tem) + i):
                if lista[x] == tem[j]:
                    regulador = True
                    j += 1
                else:
                    regulador = False
                    break
            if regulador == True:
                lista1.append(i+1)
    for e in lista1:
        print e
    print e
tem123([1,2,3])
