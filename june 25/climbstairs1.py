n = int(input())

def climb(rem, path):
    if rem == 0:
        print(*path)
        return

    if rem >= 1:
        path.append(1)
        climb(rem - 1, path)
        path.pop()

    if rem >= 2:
        path.append(2)
        climb(rem - 2, path)
        path.pop()

climb(n, [])