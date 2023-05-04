for s in[*open(0)][2::2]:
    a=*map(int,s.split()),r=i=0
    for x in a:
        i+=1
        for j in range(-i%x or x,i,x):r+=x*a[j-1]==i+j
    print(r)