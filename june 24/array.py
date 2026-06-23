import sys
sys.setrecursionlimit(200000)

def array(arr, n):
    if n == 0:
        return

    array(arr, n - 1)
    print(arr[n - 1], end=" ")

n = int(input())
arr = list(map(int, input().split()))

array(arr, n)