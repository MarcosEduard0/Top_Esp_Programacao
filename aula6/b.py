def extendedEuclid(a, b):
    global x, y, d
    if b == 0:
        x = 1
        y = 0
        d = a
        return
    extendedEuclid(b, a % b)
    x1 = y
    y1 = x - (a // b) * y
    x = x1
    y = y1


for s in [*open(0)]:
    a, b = map(int, s.split())
    x = y = d = 0
    extendedEuclid(a, b)
    print(x, y, d)
