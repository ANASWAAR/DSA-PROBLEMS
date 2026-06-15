n = int(input())
d = {}
vowels = "aeiou"
for i in range(n):
    s = input()
    a = ""
    for ch in s:
        if ch in vowels:
            a+="V"
        else:
            a+="C"
    if a not in d:
        d[a] = []
    d[a].append(s)
for a in sorted(d):
    d[a].sort()
    print(*d[a])