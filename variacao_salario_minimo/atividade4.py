# coding: utf-8


alunos = int(raw_input())
aprovados = []
reprovados = []
media1 = 0
media2 = 0
for i in range(alunos):
    nota = float(raw_input())
    if nota >= 7.0:
        aprovados.append(nota)
        media1 += nota
    else:
        reprovados.append(nota)
        media2 += nota


if len(reprovados) == 0:
    media_total = float(media1)/len(aprovados)
    porcentagem_aprov = (float(len(aprovados))*100)/float(alunos)
    print "aprovados: %d (%.2f%%)" %(len(aprovados), porcentagem_aprov)
    print "nota média aprovados: %.2f" %media_total
    print "reprovados: 0 (0.0%%)"
elif len(aprovados) == 0:
    media_total1 = float(media2)/len(reprovados)
    porcentagem_reprov = (float(len(reprovados))*100)/float(alunos)
    print "aprovados: 0 (0.0%%)"
    print "reprovados: %d (%.2f%%)" %(len(reprovados), porcentagem_reprov)
    print "nota média reprovados: %.2f" %media_total1
else:
    media_total = float(media1)/len(aprovados)
    media_total1 = float(media2)/len(reprovados)
    porcentagem_aprov = (float(len(aprovados))*100)/float(alunos)
    porcentagem_reprov = (float(len(reprovados))*100)/float(alunos)
    print "aprovados: %d (%.2f%%)" %(len(aprovados), porcentagem_aprov)
    print "nota média aprovados: %.2f" %media_total
    print "reprovados: %d (%.2f%%)" %(len(reprovados), porcentagem_reprov)
    print "nota média reprovados: %.2f" %media_total1
