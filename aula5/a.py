for s in [*open(0)][1:]:
    s = s.strip()
    print("red") if (s.count('0') and sum(int(x) % 2 == 0 for x in s)
                     > 1 and sum(int(x) for x in s) % 3 == 0) else print("cyan")
