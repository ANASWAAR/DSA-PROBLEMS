n=int(input())
a=input()
p=[0]*(n+1)
for i in range (1,n+1):
    if a[i-1] in "aeiou":
        p[i]=p[i-1]+1
    else:
        p[i]=p[i-1]
q=int(input())
for i in range (q):
    l,r=map(int,input().split())
    print(p[r]-p[l-1])