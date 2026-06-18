n=int(input())
s=input()
freq={}
l=0
ans=0
for r in range(n):
    freq[s[r]]=freq.get(s[r],0)+1
    while freq[s[r]]>1:
        freq[s[l]]-=1
        l+=1
    ans=max(ans,r-l+1)
print(ans)