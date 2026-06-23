def min(arr,n):
    if(n == 1):
        return(arr[0])
    small=min(arr,n-1)
    if(small<arr[n-1]):
        return small
    else:
        return arr[n-1]

n=int(input())
arr=list(map(int,input().split()))

print(min(arr,n))