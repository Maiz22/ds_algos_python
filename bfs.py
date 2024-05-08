from graph import Graph


def bfs(graph:Graph, root) -> list:
    """
    Bfs algorithm using a list and an index representing a 
    queue, to avoid a repeating queue.pop() at index 0.
    """
    queue = []
    visited = []

    if root:
        queue.append(root)
        idx = 0

    while idx < len(graph): 
        current = queue[idx]
        idx += 1
        if current not in visited:
            visited.append(current)
        for node in graph.adj_list[current]:
            if node not in visited:
                queue.append(node)
                visited.append(node)
    return queue