n = int(input())
a = list(map(int, input().split()))
s = set()
ans = []
for x in a:
    if x not in s:
        ans.append("YES")
        s.add(x)
    else:
        ans.append("NO")
print(*ans)