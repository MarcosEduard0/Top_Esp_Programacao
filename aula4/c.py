N = int(input())
inicial, desejado = [], []

for n in range(N):
    inicial.append(input())

for n in range(N):
    desejado.append(input())

barra = input()
initB = -1 if barra.count('1') == 0 else barra.index('1')


def getVar(ca, row, col):
    v = int(inicial[row][col]) ^ (int(barra[row]) * ca[col])
    if v == v ^ int(barra[col]):
        if v == int(desejado[row][col]):
            return None
        else:
            return False
    return v != int(desejado[row][col])


if initB < 0:
    print(0 if inicial == desejado else -1)
else:
    rowActions, colActions = [], []

    for n in range(N):
        if inicial[initB][n] != desejado[initB][n]:
            colActions.append(1)
        else:
            colActions.append(0)

    possible = True

    for n in range(N):
        inv = getVar(colActions, n, 0)

        for m in range(1, N):
            v = getVar(colActions, n, m)

            if v is not None and inv is None:
                inv = v

            if inv is not None and v is not None and inv != v:
                possible = False

        rowActions.append(1 if inv else 0)

    if possible:
        print(sum(rowActions) + sum(colActions))

        for r in range(len(rowActions)):
            if rowActions[r]:
                print("row", r)

        for c in range(len(colActions)):
            if colActions[c]:
                print("col", c)

    else:
        print(-1)
