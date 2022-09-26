# coding: utf-8
# Lucas Matos

def professores(alocacao, disciplina):
    alocacaodici = {}
    alocacaodici[disciplina] = alocacao
    print alocacaodici
    return len(alocacaodici[disciplina])

alocacao = raw_input().split()
disciplina = raw_input()
z =  professores(alocacao, disciplina)
print z

