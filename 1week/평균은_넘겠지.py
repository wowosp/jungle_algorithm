import sys

C=int(sys.stdin.readline())

for i in range(C):
    count=0
    A=list(map(int,sys.stdin.readline().split()))
    Averge=sum(A[1::])/A[0]
    for j in range(len(A)-1):
        if A[j+1]>Averge:
            count+=1
    print(f'{count/A[0]*100:.3f}%')