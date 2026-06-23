import sys
sys.setrecursionlimit(200000)

def indices(arr, n, x, i, found):
    if i == n:
        if not found:
            print(-1)
        return

    if arr[i] == x:
        print(i + 1, end=" ")
        found = True

    indices(arr, n, x, i + 1, found)


n = int(input())
arr = list(map(int, input().split()))
x = int(input())

indices(arr, n, x, 0, False)