for s in [*open(0)][1:]:
    a = *enumerate(map(int, s.split())),
    print(*(max(y-x+(i != j)for
                j, y in a)for i, x in a))
