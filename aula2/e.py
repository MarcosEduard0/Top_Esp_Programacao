stack = [0] * 30
n, aux, max_val, ind = 0, 0, -1, 0

while True:
    try:
        s = input()
    except EOFError:
        break
    n = 0
    is_s = s.split()

    print(s)

    for i in range(len(is_s)):
        stack[n] = int(is_s[i])
        n += 1

    for i in range(n - 1, -1, -1):
        max_val = -1

        for j in range(0, i + 1):
            if max_val <= stack[j]:
                max_val = stack[j]
                ind = j

        if ind != i:
            if ind != 0:
                print(n - ind, end=' ')
                for j in range(0, (ind // 2) + 1):
                    stack[j], stack[ind-j] = stack[ind-j], stack[j]

            print(n - i, end=' ')
            for j in range(0, (i // 2) + 1):
                stack[j], stack[i-j] = stack[i-j], stack[j]
    print(0)
