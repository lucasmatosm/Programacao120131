# coding: utf-8
# Lucas Matos

def agrupa_por_periodo(alunos):
    matriculas = {}
    ocorrencias = 0
    matriculas[int(alunos[0][:3])] = 1
    for i in range(1, len(turma)):
        if int(alunos[i][:3]) not in matriculas:
            matriculas[int(alunos[i][:3])] = 1
            print matriculas
        else:
            matriculas[int(alunos[i][:3])] = ocorrencias
            ocorrencias += 1 
    return matriculas

        
  
turma = [
    '0511114', '0521137', '0611001',
    '0611003', '0611004', '0621006',
    '0811007', '0811009', '0811502',
    '0811604', '0811605',
]
print agrupa_por_periodo(turma)
