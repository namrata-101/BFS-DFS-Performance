from collections import deque

# Same graph is used for both BFS and DFS
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': []
}


def bfs(start, goal):
    queue = deque([start])
    visited = set()
    nodes_expanded = 0

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    return nodes_expanded


def dfs(start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)

    return nodes_expanded


# Start and goal nodes
start = 'A'
goal = 'O'

# Run BFS and DFS only when this file is executed directly
if __name__ == "__main__":
    bfs_nodes = bfs(start, goal)
    dfs_nodes = dfs(start, goal)

    print("BFS Nodes Expanded:", bfs_nodes)
    print("DFS Nodes Expanded:", dfs_nodes)