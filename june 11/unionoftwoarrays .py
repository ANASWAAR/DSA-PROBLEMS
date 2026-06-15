n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

s = set()

for x in a:
    s.add(x)

for x in b:
    s.add(x)

ans = sorted(s)

print(len(ans))
print(*ans)