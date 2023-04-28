import sys
from collections import deque


def bfs(Adj, arestas, cols, u):
    nxts = deque([u])
    cols[u] = 0

    while nxts:
        v = nxts.popleft()

        for w in Adj[v]:
            ed = tuple(sorted([v, w]))
            if cols[w] is None:
                cols[w] = cols[v] ^ arestas[ed]
                nxts.append(w)
            else:
                if cols[w] ^ cols[v] != arestas[ed]:
                    return False

    return True

n, m = map(int, sys.stdin.readline().split())
status = [1 - int(i) for i in sys.stdin.readline().split()]
es = [[] for i in range(n)]

for i in range(m):
    line = [int(j) for j in sys.stdin.readline().split()]

    for u in line[1:]:
        es[u - 1].append(i)

Adj = [[] for _ in range(m)]

for u, v in es:
    Adj[u].append(v)
    Adj[v].append(u)

arestas = dict()

for i, e in enumerate(es):
    e.sort()
    if tuple(e) not in arestas:
        arestas[tuple(e)] = status[i]
    elif arestas[tuple(e)] != status[i]:
        print('NO')
        quit()
    else:
        pass

cols = [None] * m

for u in range(m):
    if cols[u] is None:
        if not bfs(Adj, arestas, cols, u):
            print('NO')
            quit()
        else:
            pass

print('YES')
