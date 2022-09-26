# coding: utf-8

grade = {"p1": [],
       "lp1": [],
       "ic": [],
       "calc1": [],
       "p2": ["ic", "p1", "lp1"],
       "lp2": ["ic", "p1", "lp1"],
       "grafos": ["ic", "p1", "lp1"],
       "calc2": ["calc1"],
       "edados": ["ic", "p1", "lp1", "p2", "lp2", "grafos"],
       "leda": ["ic", "p1", "lp1", "p2", "lp2", "grafos"]}

def disciplinas(grade, disciplinas_cursadas):
    # disciplinas_cursadas = [...]
    disciplinas_possiveis = []
    regulador = False
    for e in grade:
        if e not in disciplinas_cursadas:
            if grade[e] == []:
                disciplinas_possiveis.append(e)
            else:
                for x in grade[e]:
                    if x in disciplinas_cursadas:
                        regulador = True
                    else:
                        regulador = False
                        break
                if regulador == True:
                    disciplinas_possiveis.append(e)
    return disciplinas_possiveis

print disciplinas(grade, [])
print disciplinas(grade, ["ic", "p1", "lp1", "calc1"])
