import sys

K=int(sys.stdin.readline())
A=[]
sum=0

for i in range(K):
    N=int(sys.stdin.readline())
    if N==0:
        A.pop()
    else:
        A.append(N)
        
for i in A:
    sum+=i
    
print(sum)