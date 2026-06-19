n = int(input())
a = list(map(int, input().split()))
for l in range(n):
    for r in range(l, n):
        mx = a[l]
        for i in range(l, r + 1):
            mx = max(mx, a[i])
        print(mx, end=" ")