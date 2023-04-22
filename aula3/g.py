def is_slump(s):
    if len(s) < 3 or (s[0] != 'D' and s[0] != 'E'):
        return False
    i = 1
    while i < len(s) and s[i] == 'F':
        i += 1
    if i == len(s):
        return False
    if s[i] == 'G':
        return i == len(s) - 1
    return is_slump(s[i:]) and i < len(s) - 1 and s[-1] == 'G'


def is_slimp(s):
    if len(s) == 2 and s[0] == 'A' and s[1] == 'H':
        return True
    if len(s) > 2 and s[0] == 'A' and s[-1] == 'C':
        if s[1] == 'B' and is_slimp(s[2:-1]):
            return True
        return is_slump(s[1:-1])
    return False


def is_slurpy(s):
    for i in range(1, len(s)):
        if is_slimp(s[:i]) and is_slump(s[i:]):
            return True
    return False


print("SLURPYS OUTPUT")
n = int(input())
for i in range(n):
    s = input().strip()
    if is_slurpy(s):
        print("YES")
    else:
        print("NO")
print("END OF OUTPUT")