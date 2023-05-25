def dijkstra(adj, weights, s):
    queue = {u: float("inf") for u in adj}
    queue[s] = 0
    shortest_paths = {}
    predecessors = {s: None}
    while queue:
        u = min(queue, key=queue.get)
        shortest_paths[u] = queue[u]
        del queue[u]
        for v in adj[u]:
            if shortest_paths[u] + weights[(u, v)] < queue[v]:
                queue[v] = shortest_paths[u] + weights[(u, v)]
                predecessors[v] = u
    return shortest_paths, predecessors


adj = {"A": ["B", "C"], "B": ["C", "D"], "C": ["D"], "D": ["E"], "E": []}

weights = {
    ("A", "B"): 2,
    ("A", "C"): 3,
    ("B", "C"): 2,
    ("B", "D"): 2,
    ("C", "D"): 3,
    ("D", "E"): 1,
}

shortest_paths, predecessors = dijkstra(adj, weights, "A")
print(shortest_paths)
print(predecessors)
