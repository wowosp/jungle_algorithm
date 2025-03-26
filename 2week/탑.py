import sys

N=int(sys.stdin.readline())

arr=list(map(int,sys.stdin.readline().split()))

stack=[]
answer=[0]*N

for i in range(N):
    if stack:
        while True:
            if arr[i] <= stack[-1][0]:
                answer[i] = stack[-1][1]+1
                stack.append([arr[i],i])
                break
            else:
                stack.pop()
            if not stack:
                stack.append([arr[i],i])
                break
    else:
        stack.append([arr[i],i]) 

print(*answer)    
    
    
    

