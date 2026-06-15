n, q = map(int, input().split())
a = list(map(int, input().split()))

pos = {}

for i in range(n):
    pos[a[i]] = i + 1

for _ in range(q):
    x = int(input())

    if x in pos:
        print(pos[x])
    else:
        print(-1)