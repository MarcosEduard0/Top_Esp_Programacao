for s in[*open(0)][1:]:
    x,y=map(int,s.split())
    r=0
    while y:
        r+=y-x
        x//=10
        y//=10
    print(r)