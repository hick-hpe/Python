def createGraph(origin = "A"):
    graph = {}
    n = int(input("nodes: "))
    m = int(input("edges: "))
    for i in range(m):
        a, b, c = input().split()
        a = a.strip().upper()
        b = b.strip().upper()
        c = int(c)

        if a not in graph:
            graph[a] = [{
                'adj': b,
                'uv': c,
                'src': float("inf"),
                'p': ''
            }]
        else:
            graph[a].append({
                'adj': b,
                'uv': c,
                'src': float("inf"),
                'p': ''
            })
        
        if b not in graph:
            graph[b] = [{
                'adj': a,
                'uv': c,
                'src': float("inf"),
                'p': ''
            }]
        else:
            graph[b].append({
                'adj': a,
                'uv': c,
                'src': float("inf"),
                'p': ''
            })
    
    return graph

graph = createGraph()
print(graph)

def visitNode(v, graph, custos):
    for k in range(len(graph[v])):
        x = graph[v][k]
        
        if custos[x['adj']]['d'] > custos[v]['d'] + x['uv']:
            custos[x['adj']]['d'] = custos[v]['d'] + x['uv']
            custos[x['adj']]['p'] = v

    return custos
    

def get_min_custo(custos, to_visited):
    minCusto = to_visited[0]
    for u in custos:
        if not custos[u]['visited']:
            if custos[u]['d'] < custos[minCusto]['d']:
                minCusto = u
            
    custos[minCusto]['visited'] = True
    return minCusto


def dijkstra(graph):
    custos = {}
    for k in list(graph.keys()):
        custos[k] = {
            'd': float("inf"),
            'p': '',
            'visited': False,
        }
    to_visited = list(custos.keys())
    custos[to_visited[0]]['d'] = 0

    for v in graph:
        minCusto = get_min_custo(custos, to_visited)
        to_visited.remove(minCusto)
        custos = visitNode(minCusto, graph, custos)

    for c in custos:
        print(c, custos[c])

dijkstra(graph)
