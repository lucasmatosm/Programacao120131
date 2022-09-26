# coding: utf-8
# Lucas Matos

salasprofs = {
'Franklin': 206,    'Tiago':206,        'Eliane': 206,
'Adalberto':209,    'Wilkerson':207,    'Dalton': 204,
'Jorge': 204
}
def colegas_de_sala(salasprofs, professor):
	for e in salasprofs:
		for i in e:
			print i
print colegas_de_sala(salasprofs, "Franklin")
