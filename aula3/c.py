from collections import defaultdict

palavras = []
while True:
    palavra = input()
    if palavra == "#":
        break
    palavras.append(palavra)

# criando grafo direcionado
grafo = defaultdict(list)
for i in range(len(palavras) - 1):
    w1, w2 = palavras[i], palavras[i + 1]
    for j in range(min(len(w1), len(w2))):
        if w1[j] != w2[j]:
            grafo[w1[j]].append(w2[j])
            break

visitado = set()
resultado = []

# busca em profundidade
def dfs(vertice):
    visitado.add(vertice)
    for vizinho in grafo[vertice]:
        if vizinho not in visitado:
            dfs(vizinho)
    resultado.append(vertice)

for vertice in list(grafo.keys()):
    if vertice not in visitado:
        dfs(vertice)

print("".join(reversed(resultado)))
