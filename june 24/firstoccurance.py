def first(arr, n, x, i):
    if i == n:
        return -1

    if arr[i] == x:
        return i + 1

    return first(arr, n, x, i + 1)


n = int(input())
arr = list(map(int, input().split()))
x = int(input())

print(first(arr, n, x, 0))