n, k = map(int, input().split())

def climb(rem, path):
    if rem == 0:
        print(*path)
        return

    for jump in range(1, k + 1):
        if rem >= jump:
            path.append(jump)
            climb(rem - jump, path)
            path.pop()

climb(n, [])