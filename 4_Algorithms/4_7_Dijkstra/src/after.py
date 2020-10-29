import heapq

def dijkstra(start, graph):
    n = len(graph)
    heap = []
    distances = [float('inf')] * n

    def push(data):
        heapq.heappush(heap, data)
    
    def pop():
        return heapq.heappop(heap)

    push((0, start))
    distances[start] = 0

    while heap:
        dist, node = pop()

        if dist > distances[node]:
            continue

        for adj_node, adj_dist in graph[node]:
            new_dist = dist + adj_dist
            if new_dist < distances[adj_node]:
                distances[adj_node] = new_dist
                push((new_dist, adj_node))
    
    return distances
        


graph = [[(2, 5), (3, 2)], # (인접노드, 가중치)
         [(3, 5), (4, 3)],
         [(0, 3), (4, 9)],
         [(0, 10), (4, 2)],
         [(2, 13), (1, 3)]]

print(dijkstra(0, graph))