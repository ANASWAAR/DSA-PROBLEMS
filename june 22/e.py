def power(x,n):
    if n==0:
        return 1
    return x*power(x,(n-1))

def main(x,n):
    if n ==0:
        return 1
    elif(x ==0):
        return 0
    else:
        print(power(x,n))

main(3,2)