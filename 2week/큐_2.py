import sys

N=int(sys.stdin.readline())

A=[]
front=0
for i in range(N):
    M=sys.stdin.readline().split()
    if M[0] == "push":
        A.append(M[1])
    elif M[0] == "pop":
        if len(A)==front:
            print(-1)
        else:
            print(A[front])
            front+=1
                 
    elif M[0] == "size":
        print(len(A)-front)
        
    elif M[0] == "empty":
        if len(A)==front:
            print(1)
        else:
            print(0)
    elif M[0] == "front":
        if len(A)==front:
            print(-1)
        else:
            print(A[front])
    elif M[0] == "back":
        if len(A)==front:
            print(-1)
        else:
            print(A[len(A)-1])
            
            
# import sys
# from collections import deque

# N=int(sys.stdin.readline())

# A=deque()

# for i in range(N):
#     M=sys.stdin.readline().split()
#     if M[0] == "push":
#         A.append(M[1])
#     elif M[0] == "pop":
#         if len(A)==0:
#             print(-1)
#         else:
#             print(A.popleft())
                 
#     elif M[0] == "size":
#         print(len(A))
        
#     elif M[0] == "empty":
#         if len(A)==0:
#             print(1)
#         else:
#             print(0)
#     elif M[0] == "front":
#         if len(A)==0:
#             print(-1)
#         else:
#             print(A[0])
#     elif M[0] == "back":
#         if len(A)==0:
#             print(-1)
#         else:
#             print(A[len(A)-1])