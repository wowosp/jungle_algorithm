import sys

A,B=list(sys.stdin.readline().split())

if int(A[::-1])>int(B[::-1]):
    print(int(A[::-1]))
else :
    print(int(B[::-1]))