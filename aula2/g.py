from collections import Counter


def check(Sum: int) -> bool:
    if d[Sum] > 0:
        d[Sum] -= 1
        return True
    if Sum == 1:
        return False
    return check(Sum//2) and check((Sum+1)//2)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = Counter(a)
    print("Yes" if check(sum(a)) else "NO")
