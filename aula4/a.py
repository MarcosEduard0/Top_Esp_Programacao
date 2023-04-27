n, m = map(int, input().split())
vivo, vencedor = list(range(1, n + 3)), [0] * (n + 2)
for _ in range(m):
    l, r, x = map(int, input().split())
    while l < x:
        if vencedor[l]:
            vivo[l], l = x, vivo[l]
        else:
            vivo[l] = vencedor[l] = x
            l += 1
    l += 1
    r += 1
    while vencedor[r]:
        r = vivo[r]
    while l < r:
        if vencedor[l]:
            vivo[l], l = r, vivo[l]
        else:
            vivo[l], vencedor[l] = r, x
            l += 1
print(' '.join(map(str, vencedor[1: -1])))
