from collections import deque

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    # Ordenando prioridades
    tarefas = [0] * (n+1)
    adjList = [[] for _ in range(n+1)]

    for _ in range(m):
        n, m = map(int, input().split())
        adjList[n].append(m)
        tarefas[m] += 1


    # classificação topológica
    lista = deque()
    ordem = []

    for i in range(1, n+1):
        if tarefas[i] == 0:
            lista.append(i)

    while lista:
        u = lista.popleft()
        ordem.append(u)

        for v in adjList[u]:
            tarefas[v] -= 1
            if tarefas[v] == 0:
                lista.append(v)

    print(" ".join(map(str, ordem)))
