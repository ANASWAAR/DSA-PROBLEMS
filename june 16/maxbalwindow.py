N, K = map(int, input().split())
A = list(map(int, input().split()))
ones = 0
for i in range(K):
    ones += A[i]
ans = min(K, ones + 1)

for i in range(K, N):
    ones += A[i]
    ones -= A[i - K]
    ans = max(ans, min(K, ones + 1))
print(ans)