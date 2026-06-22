def print_inc(n):
    if n == 0:
        return
    
    print_inc(n - 1)
    print(n)
    
def main():
    n=int(input())
    print_inc(n)
if __name__ == "__main__":
    main()