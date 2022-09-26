# coding: utf-8
# Lucas Matos

chave1={'@':'V','a':'v','n':'o','l':'i','#':' ','4':'a','+':'u'}

def decifra(chave, mensagem):
    decifra1 = ""
    codigo = list(mensagem)
    for i in range(len(codigo)):
        if codigo[i] in chave1:
            decifra1 += chave1[codigo[i]]
    return decifra1
        
mensagem = raw_input()
print decifra(chave1, mensagem)


