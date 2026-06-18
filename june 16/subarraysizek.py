n, k = map(int, input().split())
a = list(map(int, input().split()))
sum1 = sum(a[:k])
ans = sum1
for i in range(k, n):
    sum1 += a[i]     
    sum1 -= a[i - k]
    ans = max(ans, sum1)
print(ans)