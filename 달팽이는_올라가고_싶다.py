import sys

A, B, V = map(int, sys.stdin.readline().split())

print(1+(V-A)//(A-B)+(((V-A)%(A-B))>0))