import sys

N=int(sys.stdin.readline())

def factorial(n):
    if n>0:
        return n*factorial(n-1)
    else :
        return 1

print(factorial(N))