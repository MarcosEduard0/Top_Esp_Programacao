import sys
from collections import deque


def bfs(Adj, edges, cols, u):
    nxts = deque([u])
    cols[u] = 0

    while nxts:
        v = nxts.popleft()

        for w in Adj[v]:
            ed = tuple(sorted([v, w]))
            if cols[w] is None:
                cols[w] = cols[v] ^ edges[ed]
                nxts.append(w)
            else:
                if cols[w] ^ cols[v] != edges[ed]:
                    return False

    return True


n, m = map(int, sys.stdin.readline().split())
r = [1 - int(i) for i in sys.stdin.readline().split()]
es = [[] for i in range(n)]

for i in range(m):
    line = [int(j) for j in sys.stdin.readline().split()]

    for u in line[1:]:
        es[u - 1].append(i)

Adj = [[] for i in range(m)]

for u, v in es:
    Adj[u].append(v)
    Adj[v].append(u)

edges = dict()

for i, e in enumerate(es):
    e.sort()
    if tuple(e) not in edges:
        edges[tuple(e)] = r[i]
    elif edges[tuple(e)] != r[i]:
        print('NO')
        exit()
    else:
        pass

cols = [None] * m

for u in range(m):
    if cols[u] is None:
        if not bfs(Adj, edges, cols, u):
            print('NO')
            exit()
        else:
            pass

print('YES')
