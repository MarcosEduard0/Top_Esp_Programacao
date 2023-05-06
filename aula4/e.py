import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

# Função auxiliar para contar o número de Buccaneers em uma subcadeia
def count_buccaneers(pirates, a, b):
    return pirates[a:b+1].count('1')

# Processar cada caso de teste
for case in range(1, int(input())+1):
    # Ler o número de piratas e a descrição dos piratas
    pirates = ''
    for _ in range(int(input())):
        t = int(input())
        p = input()
        pirates += p * t

    # Processar as consultas de Deus
    print(f'Case {case}:')
    query = 1
    for _ in range(1, int(input())+1):
        op, a, b = input().split()
        a, b = int(a), int(b)
        if op == 'F':
            pirates = pirates[:a] + '1'*(b-a+1) + pirates[b+1:]
        elif op == 'E':
            pirates = pirates[:a] + '0'*(b-a+1) + pirates[b+1:]
        elif op == 'I':
            new_pirates = ''
            for i in range(a, b+1):
                new_pirates += '0' if pirates[i] == '1' else '1'
            pirates = pirates[:a] + new_pirates + pirates[b+1:]
        elif op == 'S':
            count = count_buccaneers(pirates, a, b)
            print(f'Q{query}: {count}')
            query+=1


