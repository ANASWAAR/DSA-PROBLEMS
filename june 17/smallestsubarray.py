n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 0
s = 0
ans = float('inf')

for r in range(n):
    s += a[r]

    while s > k:
        ans = min(ans, r - l + 1)
        s -= a[l]
        l += 1

if ans == float('inf'):
    print(-1)
else:
    print(ans)