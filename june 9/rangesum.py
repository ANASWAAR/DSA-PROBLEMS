def naturalsum(n):
    return (n*(n+1))//2
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    ans=naturalsum(r)-naturalsum(l-1)
    print(ans)

