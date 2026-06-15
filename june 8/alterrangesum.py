n, q = map(int,input().split())
a = list(map(int,input().split()))
p = [0]*(n+1)
for i in range(1,n + 1):
    if i % 2 == 1:
        p[i]=p[i-1]+a[i-1]
    else:
        p[i]=p[i-1]-a[i-1]
for _ in range(q):
    l, r = map(int, input().split())
    ans = p[r]-p[l-1]
    if l%2==0:
        ans=-ans
    print(ans)