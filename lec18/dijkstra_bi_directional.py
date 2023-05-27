def dijkstra_bi_directional(adj, weights, s, t):
    forward_queue = {u: float("inf") for u in adj}
    forward_queue[s] = 0
    forward_shortest_paths = {}
    forward_predecessors = {s: None}

    backward_queue = {u: float("inf") for u in adj}
    backward_queue[t] = 0
    backward_shortest_paths = {}
    backward_predecessors = {t: None}

    intersection = None
    shortest_distance = float("inf")

    while forward_queue and backward_queue:
        forward_node = min(forward_queue, key=forward_queue.get)
        forward_shortest_paths[forward_node] = forward_queue[forward_node]
        del forward_queue[forward_node]

        if forward_node in backward_shortest_paths:
            distance = (
                forward_shortest_paths[forward_node]
                + backward_shortest_paths[forward_node]
            )
            if distance < shortest_distance:
                shortest_distance = distance
                intersection = forward_node

        for neighbor in adj[forward_node]:
            if forward_shortest_paths[forward_node] + weights[
                (forward_node, neighbor)
            ] < forward_shortest_paths.get(neighbor, float("inf")):
                forward_queue[neighbor] = (
                    forward_shortest_paths[forward_node]
                    + weights[(forward_node, neighbor)]
                )
                forward_predecessors[neighbor] = forward_node

        backward_node = min(backward_queue, key=backward_queue.get)
        backward_shortest_paths[backward_node] = backward_queue[backward_node]
        del backward_queue[backward_node]

        if backward_node in forward_shortest_paths:
            distance = (
                backward_shortest_paths[backward_node]
                + forward_shortest_paths[backward_node]
            )
            if distance < shortest_distance:
                shortest_distance = distance
                intersection = backward_node

        for neighbor in adj[backward_node]:
            if backward_shortest_paths[backward_node] + weights[
                (backward_node, neighbor)
            ] < backward_shortest_paths.get(neighbor, float("inf")):
                backward_queue[neighbor] = (
                    backward_shortest_paths[backward_node]
                    + weights[(backward_node, neighbor)]
                )
                backward_predecessors[neighbor] = backward_node

    path = construct_shortest_path(
        intersection, forward_predecessors, backward_predecessors
    )
    return shortest_distance, path


def construct_shortest_path(intersection, forward_predecessors, backward_predecessors):
    forward_path = []
    backward_path = []

    node = intersection
    while node is not None:
        forward_path.append(node)
        node = forward_predecessors[node]

    node = intersection
    while node is not None:
        backward_path.append(node)
        node = backward_predecessors[node]

    return forward_path[::-1] + backward_path[1:]


adj = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}

weights = {
    ("A", "B"): 2,
    ("A", "C"): 3,
    ("B", "A"): 2,
    ("B", "C"): 2,
    ("B", "D"): 2,
    ("C", "A"): 3,
    ("C", "B"): 2,
    ("C", "D"): 3,
    ("D", "B"): 2,
    ("D", "C"): 3,
    ("D", "E"): 1,
    ("E", "D"): 1,
}

shortest_distance, path = dijkstra_bi_directional(adj, weights, "A", "E")
print(shortest_distance)
print(path)
