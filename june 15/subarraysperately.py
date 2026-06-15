n = int(input())
a = list(map(int, input().split()))
for L in range(n):
    s = 0
    for R in range(L, n):
        s += a[R]
        print(s)