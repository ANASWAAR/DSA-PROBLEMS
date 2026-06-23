def reverse_array(arr, n):
    if n == 0:
        return

    print(arr[n - 1], end=" ")
    reverse_array(arr, n - 1)


n = int(input())
arr = list(map(int, input().split()))

reverse_array(arr, n)