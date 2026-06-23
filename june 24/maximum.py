import sys
sys.setrecursionlimit(200000)

def max(arr,n):
    if n==1:
        return(arr[0])
    maximum=max(arr,n-1)
    if(maximum>arr[n-1]):
        return maximum
    else:
       return arr[n-1]
n=int(input())
arr=list(map(int,input().split()))
print(max(arr,n))








