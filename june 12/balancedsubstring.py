n,q=map(int,input().split())
s=input()
vowels = "aeiouAEIOU"
p=[0]*(n+1)
for i in range(n):
    p[i+1] = p[i]
    if s[i] in vowels:
        p[i+1]+=1
for i in range(q):
    l,r=map(int,input().split())
    v=p[r]-p[l-1]
    len=r-l+1
    c=len-v
    if (v==c):
        print("Yes")
    else:
        print("No")