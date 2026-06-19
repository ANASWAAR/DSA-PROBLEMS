n = int(input())
a = list(map(int, input().split()))
freq = {}
l = 0
ans = 0
for r in range(n):
    freq[a[r]] = freq.get(a[r], 0) + 1
    while freq[a[r]] > 1:
        freq[a[l]] -= 1
        l += 1
    ans += r - l + 1
print(ans)