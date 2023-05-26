# while True:
for N in [*open(0)]:
    # N = int(input())
    N = int(N.strip())
    if N == 0:
        break

    if N < 0:
        N *= -1

    Answer = -1
    counter = 0

    i = 2
    while i * i <= N and N != 1:
        while N % i == 0:
            N //= i
            Answer = i
        if Answer == i:
            counter += 1
        i += 1

    if N != 1 and Answer != -1:
        Answer = N
    elif counter == 1:
        Answer = -1

    print(Answer)
