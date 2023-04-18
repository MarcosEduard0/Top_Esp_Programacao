T = int(input())  # lê a quantidade de casos de teste
for _ in range(T):
    n = int(input())  # lê o tamanho do array
    a = list(map(int, input().split()))  # lê o array
    a.sort()  # ordena o array em ordem crescente
    if a[n-1] - a[n-2] <= 1:
        print("YES")
    else:
        print("NO")
