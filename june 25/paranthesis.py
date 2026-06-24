import sys
sys.setrecursionlimit(200000)

n = int(input())

ans = []

def generate(open, close, path):

    if open == n and close == n:
        ans.append(path)
        return


    if open < n:
        generate(open+1, close, path+'(')


    if close < open:
        generate(open, close+1, path+')')


generate(0,0,'')

print(len(ans))
print(*ans, sep='\n')