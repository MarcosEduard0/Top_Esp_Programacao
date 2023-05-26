def dfs(graph, visited, node):
    count = 1
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(graph, visited, neighbor)

    return count


for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    max_group_size = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            group_size = dfs(graph, visited, i)
            max_group_size = max(max_group_size, group_size)

    print(max_group_size)
