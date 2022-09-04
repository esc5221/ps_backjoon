N, M, V = [int(x) for x in input().split()]

graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = [int(x) for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)

for vertice in graph:
    vertice.sort()


def dfs(v, visited, parent):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited, v)
    return visited


def bfs(v, visited, parent):
    visited[v] = True
    queue = [v]
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return visited


visited = [False for _ in range(N+1)]
dfs(V, visited, -1)

print()
visited = [False for _ in range(N+1)]
bfs(V, visited, -1)
