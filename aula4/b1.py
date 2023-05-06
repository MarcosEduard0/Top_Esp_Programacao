import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
# leitura de entrada
n, p, M, m = map(int, input().split())
complaints = [list(map(int, input().split())) for _ in range(n)]
stations = [list(map(int, input().split())) for _ in range(p)]
interfering_pairs = [list(map(int, input().split())) for _ in range(m)]

# criando grafo das estações de rádio com as interferências
graph = [[] for _ in range(p+1)]
for u, v in interfering_pairs:
    graph[u].append(v)
    graph[v].append(u)

# função para verificar se uma estação pode ser escolhida dado um nível de sinal f
def can_choose(station, f):
    l, r = stations[station-1]
    return l <= f <= r

# função para verificar se um conjunto de estações é válido
def is_valid(stations_chosen, f):
    # verifica se todas as reclamações são atendidas
    for xi, yi in complaints:
        if xi not in stations_chosen and yi not in stations_chosen:
            return False
    
    # verifica se as estações escolhidas interferem entre si
    for station in stations_chosen:
        for neighbor in graph[station]:
            if neighbor in stations_chosen:
                return False
    
    # verifica se as estações escolhidas atendem aos requisitos de sinal
    for station in stations_chosen:
        if not can_choose(station, f):
            return False
    
    # se chegamos até aqui, as estações escolhidas são válidas
    return True

# itera sobre todos os valores de f possíveis (de 1 até M) e tenta encontrar um conjunto de estações válido
for f in range(1, M+1):
    # tenta encontrar um conjunto de estações que atenda aos requisitos
    for i in range(2**p):
        # converte o índice i para uma lista de estações escolhidas
        stations_chosen = [j+1 for j in range(p) if (i >> j) & 1]
        
        # verifica se esse conjunto de estações é válido
        if is_valid(stations_chosen, f):
            # se for válido, imprime a resposta e encerra o programa
            print(len(stations_chosen), f)
            print(*stations_chosen)
            exit()

# se não encontrarmos uma solução, imprime -1
print(-1)
