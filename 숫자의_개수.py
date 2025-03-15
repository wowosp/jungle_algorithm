import sys

A=int(sys.stdin.readline())
B=int(sys.stdin.readline())
C=int(sys.stdin.readline())

product=list(str(A*B*C))

for i in range(10):
    count=0
    for j in product:
        if i==int(j):
            count+=1
    print(count)    