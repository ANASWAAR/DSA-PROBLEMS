a, b = map(int, input().split())
def factors(n):
    count = 0
    i = 1
    while i*i<=n:
        if n%i==0:
            if i*i==n:
                count=count+1
            else:
                count=count+2
        i += 1
    return count
if factors(a)>factors(b):
    print("A")
elif factors(b)>factors(a):
    print("B")
else:
    print("DRAW")