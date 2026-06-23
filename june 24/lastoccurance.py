import sys
sys.setrecursionlimit(200000)

def last(arr, n, x):
    if n == 0:
        return -1

    if arr[n-1] == x:
        return n

    return last(arr, n-1, x)

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

print(last(arr, n, x))