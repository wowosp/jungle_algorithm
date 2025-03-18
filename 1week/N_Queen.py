import sys

N = int(sys.stdin.readline())

def n_queen(row, col, diag1, diag2):
    global result
    if row == N:
        result += 1
        return

    for x in range(N):
        if col[x] or diag1[row + x] or diag2[row - x + N - 1]:
            continue

        col[x] = diag1[row + x] = diag2[row - x + N - 1] = True
        n_queen(row + 1, col, diag1, diag2)
        col[x] = diag1[row + x] = diag2[row - x + N - 1] = False
        
result=0
col = [False] * N
diag1 = [False] * (2 * N - 1)
diag2 = [False] * (2 * N - 1)

n_queen(0, col, diag1, diag2)

print(result)
