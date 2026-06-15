q = int(input())

freq = {}
distinct = 0

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]

        if x not in freq:
            freq[x] = 1
            distinct += 1
        else:
            freq[x] += 1

    elif query[0] == 2:
        x = query[1]

        if x in freq:
            freq[x] -= 1

            if freq[x] == 0:
                del freq[x]
                distinct -= 1

    elif query[0] == 3:
        print(distinct)

    else:
        x = query[1]

        if x in freq:
            print("YES")
        else:
            print("NO")