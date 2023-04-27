n, m = map(int, input().split())
alive, vencedor = [True] * (n + 2), [0] * (n + 2)
for _ in range(m):
    l, r, x = map(int, input().split())
    for i in range(l, r + 1):
        if i != x and alive[i]:
            vencedor[i] = x
            alive[i] = False
print(' '.join(map(str, vencedor[1:-1])))
