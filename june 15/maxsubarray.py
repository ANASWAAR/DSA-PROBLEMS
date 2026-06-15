n = int(input())
a = list(map(int, input().split()))
ans = []
for L in range(n):
    mx = 0
    for R in range(L, n):
        mx = max(mx, a[R])
        ans.append(str(mx))
print("\n".join(ans))