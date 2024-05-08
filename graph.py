class Graph:
    """
    Class representing a graph by taking edges and total nodes and 
    creates an adjacency matrix.
    """
    def __init__(self, edges:list[tuple], total_nodes:int) -> None:
        self.total_nodes = total_nodes
        self.adj_list = [[] for _ in range(total_nodes)]
        self.create_adj_list(edges)

    def create_adj_list(self, edges:list[tuple]) -> None:
        for node1, node2 in edges:
            self.adj_list[node1].append(node2)
            self.adj_list[node2].append(node1)

    def __len__(self) -> int:
        return self.total_nodes
    
    def __str__(self) -> str:
        result = ""
        for node, children in enumerate(self.adj_list):
            result += f"{node}: {children}\n"
        return result



if __name__ == "__main__":
    edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
    nodes_total = 5
    graph = Graph(edges, nodes_total)
    print(f"Total Nodes: {len(graph)}")
    print(f"Adjaceny List:\n{graph}")