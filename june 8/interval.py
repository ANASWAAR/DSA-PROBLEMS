q=int(input())
for i in range(q):
    t,l,r=map(int,input().split())
    if l>r:
        print (0)
    elif t==1:
        a=(r-l-1)
        if a<0:
            print(0)
        else:
            print(a)
    elif t in (2,3):
        print (r-l)
    else:
        print (r-l+1)