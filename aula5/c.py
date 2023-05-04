for i in range(int(input())):
    input()
    a = set(list(map(int, input().split())))
    if 1 not in a:
        print("YES")
    else:
        for i in a:
            if i+1 in a:
                print("NO")
                break
        else:
            print("YES")