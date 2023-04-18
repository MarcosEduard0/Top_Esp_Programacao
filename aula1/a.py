s = input()
k = len(s)
if k == 1:
    n = int(s[k-1])
else:
    n = int(s[k-2:k])
if n % 4 == 0:
    print(4)
else:
    print(0)
