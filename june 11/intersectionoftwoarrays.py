n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

ans = sorted(set(a) & set(b))

print(len(ans))
print(*ans)