def reverse(s):
    if s == "":
        return

    print(s[-1], end="")
    reverse(s[:-1])

def main():
    n = input()
    reverse(n)

if __name__ == "__main__":
    main()