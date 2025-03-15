import sys

N,X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
small=[]

for i in range(N):
    if A[i]<X:
        small.append(A[i])
        
print(*small)