from collections import defaultdict
from queue import PriorityQueue


def find_station(stations, complaint):
    # Encontra a estação com a menor restrição inferior de sinal que pode cobrir a cidade
    x, y = complaint
    print("d")
    candidates = [(stations[x][0], x), (stations[y][0], y)]
    candidates = sorted(candidates)
    for _, i in candidates:
        if complaint not in covered[i]:
            return i
    return -1


def dfs(u, color):
    # Verifica se todas as estações selecionadas são mutuamente compatíveis
    for v in graph[u]:
        if colors[v] == color:
            return False
        if colors[v] == 0:
            colors[v] = -color
            if not dfs(v, -color):
                return False
    return True


n, p, M, m = map(int, input().split())
complaints = [tuple(map(int, input().split())) for _ in range(n)]
stations = [tuple(map(int, input().split())) for _ in range(p)]
interferences = [tuple(map(int, input().split())) for _ in range(m)]

# covered[i] é um conjunto de reclamações que a estação i pode cobrir
covered = defaultdict(set)
for i, (li, ri) in enumerate(stations):
    for j, complaint in enumerate(complaints):
        x, y = complaint
        if li <= M and li <= min(stations[x][1], stations[y][1]):
            covered[i].add(j)

# graph[i] é um conjunto de estações que interferem com a estação i
graph = [[] for _ in range(p)]
for i, (ui, vi) in enumerate(interferences):
    ui -= 1
    vi -= 1
    graph[ui].append(vi)
    graph[vi].append(ui)

# colors[i] é a cor (1 ou -1) atribuída à estação i durante a coloração de grafos
colors = [0] * p
stations_selected = set()
for j, complaint in enumerate(complaints):
    i = find_station(stations, complaint)
    if i == -1:
        print("-1")
        exit()
   
