n,k = map(int, input().split())
s = input()
def vowel(ch):
    return ch in "aeiouAEIOU"
count = 0
for i in range(k):
    if vowel(s[i]):
        count += 1
ans = [count]
for i in range(k, n):
    if vowel(s[i]):
        count += 1
    if vowel(s[i - k]):
        count -= 1
    ans.append(count)
print(*ans)