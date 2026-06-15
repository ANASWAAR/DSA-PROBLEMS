q = int(input())
freq = {}
for _ in range(q):
    typ, x = map(int, input().split())

    if typ == 1:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    elif typ == 2:
        if x in freq:
            freq[x] -= 1

            if freq[x] == 0:
                del freq[x]
    else:
        if x in freq:
            print(freq[x])
        else:
            print(0)