# coding: utf-8
# Lucas Matos

contas = { 'Ana':1000, 'Antonio':-500, 
'William':0, 'Carlos':2500, 'Kate':-1300 }
def devedores(contas):
    contador = 0
    devedor = contas.values()
    for i in range(len(devedor)):
        if float(devedor[i]) < 0:
            contador += 1
    return contador

print devedores(contas)
