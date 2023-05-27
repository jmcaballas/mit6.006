def bellman_ford(adj, weights, s):
    shortest_paths = {}
    predecessors = {}

    for v in adj:
        shortest_paths[v] = float("inf")
        predecessors[v] = None
    shortest_paths[s] = 0

    for _ in range(1, len(adj)):
        for edge in weights:
            u, v = edge
            if shortest_paths[u] + weights[edge] < shortest_paths[v]:
                shortest_paths[v] = shortest_paths[u] + weights[edge]
                predecessors[v] = u

    for edge in weights:
        u, v = edge
        if shortest_paths[u] + weights[edge] < shortest_paths[v]:
            raise Exception("Negative weight cycle exists")

    return (shortest_paths, predecessors)


adj = {"A": ["B", "C"], "B": ["C", "D"], "C": ["D"], "D": ["E"], "E": []}

weights = {
    ("A", "B"): 2,
    ("A", "C"): 3,
    ("B", "C"): 2,
    ("B", "D"): 2,
    ("C", "D"): 3,
    ("D", "E"): 1,
}

shortest_paths, predecessors = bellman_ford(adj, weights, "A")
print(shortest_paths)
print(predecessors)

adj = {"A": ["B", "C"], "B": ["C", "D"], "C": ["D"], "D": ["E"], "E": []}

weights = {
    ("A", "B"): 2,
    ("A", "C"): -3,
    ("B", "C"): 2,
    ("B", "D"): -2,
    ("C", "D"): 3,
    ("D", "E"): 1,
}

shortest_paths, predecessors = bellman_ford(adj, weights, "A")
print(shortest_paths)
print(predecessors)


adj = {"A": ["B", "C"], "B": ["C", "D"], "C": ["D"], "D": ["E"], "E": ["A"]}

weights = {
    ("A", "B"): 2,
    ("A", "C"): 3,
    ("B", "C"): 2,
    ("B", "D"): 2,
    ("C", "D"): 3,
    ("D", "E"): 1,
    ("E", "A"): -6,
}
shortest_paths, predecessors = bellman_ford(adj, weights, "A")
