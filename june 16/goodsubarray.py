n,k,t=map(int,input().split())
a=list(map(int,input().split()))
target=k*t
sum=0
for i in range (k):
    sum=sum+a[i]
count=0
if sum>=target:
    count=count+1

for i in range(k,n):
    sum+=a[i]

    sum-=a[i - k]
    if sum>=target:
        count+=1
print(count)