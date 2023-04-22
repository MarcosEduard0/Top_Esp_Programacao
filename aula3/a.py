for _ in range(int(input())):
    n, *x = map(int, input().split())
    x.sort()
    mediana = x[n // 2]
    print(sum(abs(mediana - xi) for xi in x))