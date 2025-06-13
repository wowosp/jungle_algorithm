import sys

num = sys.stdin.readline()
size = len(num)
k = 1
solve = 0

if (num[0] == '0'):   
    if (num[1]=='x'):
        for i in range(2,size-1):
            if num[size-2-(i-2)] == 'a':
                solve += int(10 * k)
            elif num[size-2-(i-2)] == 'b':
                solve += int(11 * k)
            elif num[size-2-(i-2)] == 'c':
                solve += int(12 * k)
            elif num[size-2-(i-2)] == 'd':
                solve += int(13 * k)
            elif num[size-2-(i-2)] == 'e':
                solve += int(14 * k)
            elif num[size-2-(i-2)] == 'f':
                solve += int(15 * k)
            else:
                solve += int(num[size-2-(i-2)]) * k
            k *= 16
    else:
        for i in range(1,size-1):
            solve += int(num[size-2-(i-1)]) * k
            k *= 8
else:
    for i in range(size-1):
            solve += int(num[size-2-i]) * k
            k *= 10

print(solve)