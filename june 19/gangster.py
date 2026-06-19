n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

path = []

for i in range(n - 1, -1, -1):
    path.append(a[i][0])

for j in range(1, m):
    path.append(a[0][j])

for i in range(1, n):
    path.append(a[i][m - 1])

for j in range(m - 2, 0, -1):
    path.append(a[n - 1][j])

for x in path:
    if x == -1:
        break
    print(x, end=' ')






 