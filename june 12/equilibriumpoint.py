n = int(input())
a = list(map(int, input().split()))
total=sum(a)
left=0
ans=0
for i in range(n):
    left=left+a[i]
    right=total-(left-a[i])
    if left==right:
        ans=ans+1
print(ans)