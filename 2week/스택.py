import sys

N=int(sys.stdin.readline())

A=[]

for i in range(N):
    M=sys.stdin.readline().split()
    if M[0] == "push":
        A.append(M[1])
    elif M[0] == "pop":
        if len(A)==0:
            print(-1)
        else:
            print(A.pop())
    elif M[0] == "size":
        print(len(A))
    elif M[0] == "empty":
        if len(A)==0:
            print(1)
        else:
            print(0)
    elif M[0] == "top":
        if len(A)==0:
            print(-1)
        else:
            print(A[len(A)-1])
        
        
        
            