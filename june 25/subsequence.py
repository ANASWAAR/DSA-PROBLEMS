import sys
sys.setrecursionlimit(200000)

n = int(input())
arr = list(map(int, input().split()))

ans = []

def subseq(i, path):
    if i == n:
        if path:
            ans.append(" ".join(map(str, path)))
        return

    path.append(arr[i])
    subseq(i + 1, path)
    path.pop()

    subseq(i + 1, path)

subseq(0, [])

print("\n".join(ans))