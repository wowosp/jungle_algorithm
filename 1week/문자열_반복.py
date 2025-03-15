import sys

T=int(sys.stdin.readline())

for i in range(T):
    R,S = sys.stdin.readline().split()
    for j in S:
        print(f'{int(R)*j}', end='')
    print()    