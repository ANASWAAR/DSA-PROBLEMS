import sys
sys.setrecursionlimit(200000)

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = []

def subseq(i, path, sm):
    if i == n:
        if sm == k:
            ans.append(path[:])
        return

    path.append(arr[i])
    subseq(i+1, path, sm+arr[i])
    path.pop()

    subseq(i+1, path, sm)

subseq(0, [], 0)

print(len(ans))

for x in ans:
    print(*x)