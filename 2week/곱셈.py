import sys

A,B,C=map(int,sys.stdin.readline().split())

def pow(x, k):
    if k == 0: return 1
    tmp = pow(x, k//2)%C
    if k % 2: 
        return x%C*tmp*tmp
    else: 
        return tmp*tmp
    
print(pow(A,B)%C)