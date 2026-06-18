n, k = map(int, input().split())
a = list(map(int, input().split()))

def is_prime(x):
    if x < 2:
        return False

    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1

    return True

p = []
for x in a:
    if is_prime(x):
        p.append(1)
    else:
        p.append(0)

curr = 0
for i in range(k):
    curr += p[i]

best = curr
start = 0

for i in range(k, n):
    curr += p[i]
    curr -= p[i - k]

    if curr > best:
        best = curr
        start = i - k + 1
for i in range(start, start + k):
    print(a[i], end=" ")