n,q,k=map(int,input().split())
a=list(map(int,input().split()))
p=[0]*(n+1)
def digit_sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s
p = [0]*(n+1)
for i in range(1,n+1):
    if digit_sum(a[i-1]) == k:
        p[i] = p[i-1] + 1
    else:
        p[i] = p[i-1]
for _ in range(q):
    l,r = map(int,input().split())
    print(p[r] - p[l-1])        