import sys

N=int(sys.stdin.readline())
A=[]

for i in range(N):
    score=0
    upper=0
    A=sys.stdin.readline()
    for j in range(len(A)):
        if A[j]=='O' and A[j]==A[j-1]:
            upper+=1
        else:
            upper=0
        if A[j]=='O':
            score+=1+upper
    print(score)