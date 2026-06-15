n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
freq = {}
for x in a:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
ans = []
for x in b:
    if x in freq and freq[x] > 0:
        ans.append(x)
        freq[x] -= 1

ans.sort()
print(len(ans))
print(*ans)