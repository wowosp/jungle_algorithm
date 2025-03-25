import sys

N = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

blue = 0
white = 0


def check_color(arr, row, col, n):
    check = arr[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if check != arr[i][j]:
                return False
    return True


def find_BW(arr, row, col, n):
    global blue, white
    if check_color(arr, row, col, n):
        if arr[row][col] == 1:
            blue += 1
            return
        else:
            white += 1
            return

    half = n // 2
    find_BW(arr, row, col, half)
    find_BW(arr, row, col + half, half)
    find_BW(arr, row + half, col, half)
    find_BW(arr, row + half, col + half, half)


find_BW(A, 0, 0, N)

print(white)
print(blue)
