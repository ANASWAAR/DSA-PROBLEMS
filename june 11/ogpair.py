s = input().strip()
o_count = 0
ans = 0
for ch in s:
    if ch == 'O':
        o_count += 1
    elif ch == 'G':
        ans += o_count

print(ans)