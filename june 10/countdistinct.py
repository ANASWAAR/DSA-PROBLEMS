n = int(input())
a = list(map(int, input().split()))
freq = {}
for x in a:
    freq[x] = 1
print(len(freq))