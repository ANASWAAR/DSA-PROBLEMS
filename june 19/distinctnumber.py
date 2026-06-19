n = int(input())
a = list(map(int, input().split()))
k = int(input())

freq = {}

for i in range(k):
    freq[a[i]] = freq.get(a[i], 0) + 1

ans = [len(freq)]

for i in range(k, n):
  
    freq[a[i]] = freq.get(a[i], 0) + 1

    freq[a[i - k]] -= 1
    if freq[a[i - k]] == 0:
        del freq[a[i - k]]

    ans.append(len(freq))
print(*ans)