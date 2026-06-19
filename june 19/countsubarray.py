n = int(input())
a = list(map(int, input().split()))
k = int(input())

freq = {0: 1}
s = 0
count = 0

for x in a:
    s += x

    count += freq.get(s - k, 0)
    freq[s] = freq.get(s, 0) + 1
print(count)