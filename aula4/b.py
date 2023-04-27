# import os
# import sys
# def input(): return sys.stdin.readline().rstrip("\r\n")


def find_SCC(graph):
    SCC, S, P = [], [], []
    depth = [0] * len(graph)
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            d = depth[~node] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                del S[d:], P[-1]
                for node in SCC[-1]:
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
    SCC = SCC[::-1]
    cx = [-1] * len(graph)
    for i in range(len(SCC)):
        for j in SCC[i]:
            cx[j] = i
    return cx


for _ in range(int(input()) if not True else 1):
    n, p, M, m = map(int, input().split())
    graph = [[] for __ in range(2 * p + 2 * M + 1)]
    for i in range(n):
        x, y = map(int, input().split())
        x2 = (x + p)
        y2 = (y + p)
        graph[x2] += [y]
        graph[y2] += [x]
    for x in range(1, p + 1):
        l, r = map(int, input().split())
        x2 = (x + p)
        l += 2 * p
        r += 2 * p + 1
        graph[l+M] += [x2]
        graph[x] += [l]
        if r + M != 2 * p + 2 * M + 1:
            graph[r] += [x2]
            graph[x] += [r + M]
    for i in range(m):
        x, y = map(int, input().split())
        x2 = (x + p)
        y2 = (y + p)
        graph[x] += [y2]
        graph[y] += [x2]
    for i in range(1, M):
        graph[2 * p + i + M] += [2 * p + i + M + 1]
        graph[2 * p + i + 1] += [2 * p + i]
    cx = find_SCC(graph)
    ans = []
    for i in range(1, p + 1):
        if cx[i] > cx[i + p]:
            ans += [i]
    if not ans:
        print(-1)
        quit()
    for freq in range(M, 0, -1):
        if cx[2 * p + freq] > cx[2 * p + freq + M]:
            break
    print(len(ans), freq)
    print(*ans)
