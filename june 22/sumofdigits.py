def summ(n):
    if n == 0:
        return 0

    return (n % 10) + summ(n // 10)


n = int(input())
print(summ(n))