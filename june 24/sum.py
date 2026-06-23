def sum(arr,n):
    if n==1:
        return(arr[0])
    s=0
    s=sum(arr,n-1)
    s+=arr[n-1]
    return s
n=int(input())
arr=list(map(int,input().split()))
print(sum(arr,n))