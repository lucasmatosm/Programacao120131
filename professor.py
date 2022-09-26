# coding: utf-8
# Lucas Matos

alocacao = {"P1": ['Jorge', 'Dalton','Wilkerson'],
         "IC": ['Andrey', 'Joseana'],
         "P2": ['Livia', 'Raquel', 'Nazareno'],
         "LPT": ['Marli']}
         
def professores(alocacao, disciplina):
    if disciplina not in alocacao:
        return "Nao ha professores"
    else:
        return len(alocacao[disciplina])

disciplina = raw_input()
print professores(alocacao, disciplina)        
