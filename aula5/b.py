def GetPrimes(n):
    x = 2
    primes = dict()
    while n > 1:
        if n % x == 0:
            primes[x] = primes.get(x, 0) + 1
            n //= x
        elif n < x * x:
            primes[n] = primes.get(n, 0) + 1
            break
        else:
            x += 1
    return primes


def Solve(k, cs):
    pps = set([pr**pw for pr, pw in GetPrimes(k).items()])
    for c in cs:
        for_del = set()
        for pp in pps:
            if c % pp == 0:
                for_del.add(pp)
        for pp in for_del:
            pps.remove(pp)
    return len(pps) == 0
    

n, k = map(int, input().split())
cs = set(map(int, input().split()))
print('Yes' if Solve(k, cs) else 'No')