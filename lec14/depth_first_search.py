def dfs_visit(adj, s, parents, finish_times):
    for v in adj[s]:
        if v not in parents:
            parents[v] = s
            dfs_visit(adj, v, parents, finish_times)
    finish_times.append(s)


def dfs(adj):
    parents = {}
    finish_times = []

    for s in adj:
        if s not in parents:
            parents[s] = None
            dfs_visit(adj, s, parents, finish_times)

    return (parents, finish_times)


def topological_sort(finish_times):
    return list(reversed(finish_times))


adj = {0: [1, 3], 1: [2, 4], 2: [3, 5], 3: [4], 4: [5], 5: []}
print(adj)
dfs_output, finish_times = dfs(adj)
print(dfs_output)
print(topological_sort(finish_times))
