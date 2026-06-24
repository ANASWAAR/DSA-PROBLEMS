n, m = map(int, input().split())

def paths(i, j, path):

    if i == n and j == m:
        print(path)
        return


    if j < m:
        paths(i, j+1, path + 'R')


    if i < n:
        paths(i+1, j, path + 'D')


paths(1, 1, "")