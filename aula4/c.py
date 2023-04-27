N = int(input())
a, b = [], []

for n in range(N):
    a.append(input())

for n in range(N):
    b.append(input())

wand = input()
piv = -1 if wand.count('1') == 0 else wand.index('1')


def getVar(ca, row, col):
    v = int(a[row][col]) ^ (int(wand[row]) * ca[col])
    if v == v ^ int(wand[col]):
        if v == int(b[row][col]):
            return None
        else:
            return False
    return v != int(b[row][col])


if piv < 0:
    print(0 if a == b else -1)
else:
    rowActions, colActions = [], []

    for n in range(N):
        if a[piv][n] != b[piv][n]:
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
