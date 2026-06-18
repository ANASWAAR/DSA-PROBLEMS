n,k=map(int,input().split())
s=input()
freq={}
l=0
ans=0
for r in range(n):
    freq[s[r]]=freq.get(s[r],0)+1
    while len(freq)>k:
        freq[s[l]]-=1
        if freq[s[l]]==0:
            del freq[s[l]]
        l+=1
    ans=max(ans,r-l+1)
print(ans)
