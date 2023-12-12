from grafo import grafo

def largura(vs, valor):
    for v in  vs:
        if v == valor:
            return True
    filhos = []
    for v in vs:
        filhos.extend(grafo[v])
    largura(filhos, valor)