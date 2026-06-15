n,q,k=map(int,input().split())
a=list(map(int,input().split()))
p=[0]*(n+1)
def count_fac(x):
    count=0
    for i in range (1,int(x**0.5)+1):
        if x%i==0:
            count+=1
            if i != x // i:
                count += 1
    return count
p = [0]*(n+1)
for i in range(1,n+1):
    if count_fac(a[i-1]) == k:
        p[i] = p[i-1] + 1
    else:
        p[i] = p[i-1]
for _ in range(q):
    l,r = map(int,input().split())
    print(p[r] - p[l-1])        