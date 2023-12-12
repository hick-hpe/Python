from grafo import grafo

def profundidade(v, val):
    achou = False
    if v == val:
        return True
    for i in v.adj:
        if profundidade(i, val):
            achou = True
    return achou