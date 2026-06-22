def zigzag(n):
    if n == 0:
        return

    print(n)
    zigzag(n - 1)
    if n!=1:
        print(n)
def main():
    n=int (input())
    zigzag(n)
if __name__=="__main__":
    main()