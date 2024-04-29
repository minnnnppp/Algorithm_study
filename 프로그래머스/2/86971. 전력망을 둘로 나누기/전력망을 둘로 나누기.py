from collections import deque
def bfs(start, graph):
    queue = deque()
    count = 1
    visited = [False] * len(graph)

    queue.append(start)
    visited[start] = True

    while queue:
        current = queue.popleft()
        if graph[current] is not None:
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    count += 1
    return count

def solution(n, wires):
    min_diff = float('inf')
    graph = [[] for _ in range(n + 1)]

    for node1, node2 in wires:
        graph[node1].append(node2)
        graph[node2].append(node1)

    for node1, node2 in wires:
        graph[node1].remove(node2)
        graph[node2].remove(node1)
        diff = abs(bfs(node1, graph) - bfs(node2, graph))
        min_diff = min(min_diff, diff)
        graph[node1].append(node2)
        graph[node2].append(node1)

    return min_diff