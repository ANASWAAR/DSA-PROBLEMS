n, target = map(int, input().split())
a = list(map(int, input().split()))
mp = {}
for i in range(n):
    req = target - a[i]
    if req in mp:
        print(mp[req], i + 1)
        break
    mp[a[i]] = i + 1
else:
    print(-1)