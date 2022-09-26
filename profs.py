# coding: utf-8
# Lucas Matos

salasprofs = {
'Franklin': 206,    'Tiago':206,        'Eliane': 206,
'Adalberto':209,    'Wilkerson':207,    'Dalton': 204,
'Jorge': 204
}
def  colegas_de_sala(salasprofs, professor):
    sala = []
    if professor in salasprofs:
        for e in salasprofs:
            if salasprofs[e] == salasprofs[professor]:
                sala.append(e)
        sala.remove(professor)
        return sala
    else:
        return sala 

print colegas_de_sala(salasprofs, 'Franklin')
print colegas_de_sala(salasprofs, 'Adalberto')
