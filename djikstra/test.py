import heapq
import sys

def constructAdj(edges, V):
    adj = [[] for _ in range(V)]
    for u, v, wt in edges:
        adj[u].append([v, wt])
        adj[v].append([u, wt])
    return adj

def dijkstra(V, edges, src):
    adj = constructAdj(edges, V)

    pq = []                      # Min-heap
    dist = [sys.maxsize] * V     # Эхэндээ бүх зайг INFINITY болгоно

    heapq.heappush(pq, (0, src))
    dist[src] = 0

    while pq:
        d, u = heapq.heappop(pq)

        # Хэрэв хуучин утга байвал алгасана (optional optimization)
        if d > dist[u]:
            continue

        for v, weight in adj[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist


if __name__ == "__main__":
    V = 5
    src = 0
    edges = [
        [0, 1, 4],
        [0, 2, 8],
        [1, 4, 6],
        [2, 3, 2],
        [3, 4, 10]
    ]

    result = dijkstra(V, edges, src)
    print(' '.join(map(str, result)))
