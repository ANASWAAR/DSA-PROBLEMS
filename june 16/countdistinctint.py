n, k = map(int, input().split())
a = list(map(int, input().split()))
freq = {}
for i in range(k):
    freq[a[i]] = freq.get(a[i], 0) + 1
ans = [len(freq)]
for i in range(k, n):
    freq[a[i]] = freq.get(a[i], 0) + 1
    x = a[i - k]
    freq[x] -= 1
    if freq[x] == 0:
        del freq[x]
    ans.append(len(freq))
print(*ans)