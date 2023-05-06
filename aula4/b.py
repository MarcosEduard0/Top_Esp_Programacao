import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def find_strongly_connected_components(graph):
    scc = []
    S = []
    P = []
    depth = [0] * len(graph)
    stack = list(range(len(graph)))

    while stack:
        node = stack.pop()

        if node < 0:
            d = depth[~node] - 1

            if P[-1] > d:
                scc.append(S[d:])
                del S[d:]
                del P[-1]

                for node in scc[-1]:
                    depth[node] = -1

        elif depth[node] > 0:
            while P[-1] > depth[node]:
                P.pop()

        elif depth[node] == 0:
            S.append(node)
            P.append(len(S))
            depth[node] = len(S)
            stack.append(~node)
            stack += graph[node]

    scc = scc[::-1]
    component_index = [-1] * len(graph)

    for i in range(len(scc)):
        for j in scc[i]:
            component_index[j] = i

    return component_index


for _ in range(int(input()) if not True else 1):
    n, p, M, m = map(int, input().split())

    graph = [[] for _ in range(2 * p + 2 * M + 1)]

    for i in range(n):
        x, y = map(int, input().split())
        x2 = (x + p)
        y2 = (y + p)
        graph[x2].append(y)
        graph[y2].append(x)

    for x in range(1, p + 1):
        l, r = map(int, input().split())
        x2 = (x + p)
        l += 2 * p
        r += 2 * p + 1
        graph[l+M].append(x2)
        graph[x].append(l)

        if r + M != 2 * p + 2 * M + 1:
            graph[r].append(x2)
            graph[x].append(r + M)

    for i in range(m):
        x, y = map(int, input().split())
        x2 = (x + p)
        y2 = (y + p)
        graph[x].append(y2)
        graph[y].append(x2)

    for i in range(1, M):
        graph[2 * p + i + M].append(2 * p + i + M + 1)
        graph[2 * p + i + 1].append(2 * p + i)

    component_index = find_strongly_connected_components(graph)
    ans = []

    for i in range(1, p + 1):
        if component_index[i] > component_index[i + p]:
            ans.append(i)

    if not ans:
        print(-1)
        break

    for freq in range(M, 0, -1):
        if component_index[2 * p + freq] > component_index[2 * p + freq + M]:
            break

    print(len(ans), freq)
    print(*ans)
