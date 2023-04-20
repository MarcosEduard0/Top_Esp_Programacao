from collections import deque
from itertools import count


def team_queue(t, teams):
    # Dicionário para armazenar a equipe de cada pessoa
    team_of = {}
    for i in range(t):
        for elem in teams[i]:
            team_of[elem] = i

    # Lista de deques, uma para cada time
    team_queues = [deque() for _ in range(t)]
    # Lista de equipes, ordem de chegada
    fila_equipe = deque()

    # Verificando comandos
    while True:
        command = input()
        if command.startswith('S'):
            return
        elif command.startswith('E'):
            x = int(command.split()[-1])
            team = team_of[x]
            if len(team_queues[team]) == 0:
                fila_equipe.append(team)
            team_queues[team].append(x)
        else:
            primeira_equipe = fila_equipe[0]
            print(f"{team_queues[primeira_equipe].popleft()}")
            if len(team_queues[primeira_equipe]) == 0:
                fila_equipe.popleft()


for case in count(1):
    t = int(input())
    if t == 0:
        break
    print(f"Scenario #{case}")
    teams = [list(map(int, input().split()[1:])) for _ in range(t)]
    team_queue(t, teams)
    print()
