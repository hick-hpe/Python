import heapq

def prim(graph, start=0):
    mst = []  # Lista para armazenar as arestas da MST
    visited = [False] * len(graph)  # Array para verificar se o nó foi visitado
    min_heap = [(0, start, -1)]  # Fila de prioridade (peso, nó atual, nó anterior)
    total_cost = 0  # Custo total da MST

    while min_heap:
        cost, u, prev = heapq.heappop(min_heap)  # Seleciona a aresta de menor peso
        if visited[u]:
            continue  # Se o nó já foi visitado, ignore
        
        visited[u] = True
        if prev != -1:
            mst.append((prev, u, cost))  # Adiciona a aresta à MST
            total_cost += cost  # Adiciona o custo da aresta ao custo total
        
        for weight, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v, u))
    
    return total_cost, mst

# Exemplo de uso:
# Grafo representado como uma lista de adjacências
# Cada elemento é uma lista de tuplas (peso, nó)
graph = [
    [(1, 1), (4, 2)],  # Nó 0: arestas (peso, nó) para nó 1 e nó 2
    [(1, 0), (2, 2), (3, 3)],  # Nó 1
    [(4, 0), (2, 1), (5, 3)],  # Nó 2
    [(3, 1), (5, 2)]  # Nó 3
]

# Chama a função prim e imprime o custo total da MST e as arestas da MST
total_cost, mst = prim(graph)
print("Custo total da MST:", total_cost)
print("Arestas na MST:", mst)
