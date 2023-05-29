from collections import defaultdict


def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


# Take graph and starting node as user input
num_nodes = int(input("Enter the number of nodes in the graph: "))
graph = defaultdict(list)

for _ in range(num_nodes):
    node = input("Enter a node: ")
    num_neighbors = int(input(f"Enter the number of Childs for node {node}: "))

    for _ in range(num_neighbors):
        neighbor = input("Enter a neighbor: ")
        graph[node].append(neighbor)

start_node = input("Enter the starting node: ")

# Perform BFS and DFS
print("BFS traversal:")
bfs(graph, start_node)

print("\nDFS traversal:")
dfs(graph, start_node)
