from graph import Graph


def dfs(graph:Graph, root) -> list:
    stack = []
    visited = []
    result = []

    if root:
        stack.append(root)

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            result.append(current)
        for node in graph.adj_list[current]:
            if node not in visited:
                stack.append(node)
    return result