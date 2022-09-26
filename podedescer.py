# coding: utf-8
# Lucas Matos

def pode_descer(labirinto):
    for j in range(len(labirinto[0])):
        for i in range(len(labirinto)):
                if labirinto[i][j] == "*" and i != (len(labirinto)-1):
                    if labirinto[i+1][j] != "P":
                        return True
                    else:
                        return False
                
    return False
labirinto1 = [
  ['P', '*', ' ', ' '],
  ['P', ' ', 'P', ' '],
  ['P', 'P', 'P', ' '],
]
labirinto2 = [
  ['P', ' ', '*', ' '],
  ['P', ' ', 'P', ' '],
  ['P', 'P', 'P', ' '],
]
print pode_descer(labirinto1)
print pode_descer(labirinto2)
