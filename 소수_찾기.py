import sys
import math

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

for i in A:
    if i == 1:
        N-=1
        continue
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            N-=1
            break

print(N)