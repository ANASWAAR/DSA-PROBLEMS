n, m, k = map(int, input().split())
a = list(map(int, input().split()))
m = set(map(int, input().split()))
count = 0
for i in range(k):
    if a[i] in m:
        count += 1
ans = [count]
for i in range(k, n):
    if a[i] in m:
        count += 1
    if a[i - k] in m:
        count -= 1
    ans.append(count)
print(*ans)