from collections import deque

def bfs(Adj, arestas, cols, u):
    nxts = deque([u])
    cols[u] = 0

    while nxts:
        v = nxts.popleft()

        for w in Adj[v]:
            ed = frozenset([v, w])
            if cols[w] is None:
                cols[w] = cols[v] ^ arestas[ed]
                nxts.append(w)
            elif cols[w] ^ cols[v] != arestas[ed]:
                return False

    return True

n, m = map(int, input().split())
status = [1 - int(i) for i in input().split()]
es = [[] for _ in range(n)]

for i in range(m):
    line = list(map(int, input().split()))[1:]
    for u in line:
        es[u - 1].append(i)

Adj = [[] for _ in range(m)]

for u, v in es:
    Adj[u].append(v)
    Adj[v].append(u)
    
arestas = dict()
arestas = {frozenset(e): status[i] for i, e in enumerate(es) if frozenset(e) not in arestas or arestas[frozenset(e)] == status[i]}

cols = [None] * m

for u in range(m):
    if cols[u] is None and not bfs(Adj, arestas, cols, u):
        print('NO')
        quit()

print('YES')
