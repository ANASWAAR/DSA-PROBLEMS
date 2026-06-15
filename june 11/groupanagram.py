n = int(input())
groups = {}
for _ in range(n):
    s = input().strip()
    key = ''.join(sorted(s))
    if key not in groups:
        groups[key] = []
    groups[key].append(s)
print(len(groups))
for key in sorted(groups):
    groups[key].sort()
    print(len(groups[key]), *groups[key])