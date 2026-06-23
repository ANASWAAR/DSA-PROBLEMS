import sys
sys.setrecursionlimit(200000)
def sorted(arr, n):
    if n == 1:
        return True

    if arr[n-2] > arr[n-1]:
        return False

    return sorted(arr, n-1)


n = int(input())
arr = list(map(int, input().split()))

if sorted(arr, n):
    print("YES")
else:
    print("NO")