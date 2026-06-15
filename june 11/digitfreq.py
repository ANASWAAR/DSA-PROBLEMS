n = input()

freq = [0] * 10

for ch in n:
    digit = int(ch)
    freq[digit] += 1

for i in range(10):
    print(freq[i], end=" ")