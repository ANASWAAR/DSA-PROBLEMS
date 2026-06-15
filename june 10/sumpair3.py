n, x = map(int, input().split())
a = list(map(int, input().split()))
freq = {}
count = 0
for num in a:
    req = x - num
    if req in freq:
        count += freq[req]
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(count)