n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

def paths(i, j, path):

    if i == n-1 and j == m-1:
        print(path)
        return

    # Move Right
    if j + 1 < m and grid[i][j+1] == 0:
        paths(i, j+1, path + 'R')

    # Move Down
    if i + 1 < n and grid[i+1][j] == 0:
        paths(i+1, j, path + 'D')


paths(0, 0, "")