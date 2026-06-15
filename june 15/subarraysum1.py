n = int(input())
a = list(map(int, input().split()))
ans = 0
for L in range(n):
    s = 0
    for R in range(L, n):
        s += a[R]
        ans += s
print(ans)