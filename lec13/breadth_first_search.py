from random import choice


def bfs(adj, s):
    levels = {s: 0}
    parents = {s: None}
    i = 1
    frontier = [s]

    while frontier:
        next_level = []
        for u in frontier:
            for v in adj[u]:
                if v not in levels:
                    levels[v] = i
                    parents[v] = u
                    next_level.append(v)
        frontier = next_level
        i += 1

    return (levels, parents)


def generate_adjacency_list(vertices, edges):
    adj = {str(i): [] for i in range(vertices)}
    vertices = list(adj.keys())

    for _ in range(edges):
        v1 = choice(vertices)
        v2 = choice(vertices)

        if v1 != v2 and v2 not in adj[v1]:
            adj[v1].append(v2)
            adj[v2].append(v1)

    return adj


adj = generate_adjacency_list(5, 6)
print(adj)
levels, parents = bfs(adj, list(adj.keys())[0])
print(levels)
print(parents)
