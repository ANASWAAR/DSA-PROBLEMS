n=int(input())
a=list(map(int,input().split()))
p=[0]*n
p[0]=a[0]
for i in range(1,n):
    p[i]=p[i-1]+a[i]
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    if l==1:
        print(p[r-1])
    else:
        print(p[r-1]-p[l-2])