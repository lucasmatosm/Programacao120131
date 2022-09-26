# coding: utf-8
# Lucas Matos
splab = {1313:['Franklin', 'Jorge'], 1226:['Eliane', 'Dalton'], 1507:['Wilkerson'] }

def senha(cadastro, usuario):
    for i in splab:
        for e in splab[i]:
            if usuario in splab[i]:
                return i
            return -1
usuario = raw_input()
print senha(splab, usuario)
