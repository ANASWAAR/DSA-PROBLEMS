from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

freq = defaultdict(int)
ans = 0

for x in a:
    ans += freq[x]
    freq[x * k] += 1

print(ans)