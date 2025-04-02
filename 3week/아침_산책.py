import sys

N= int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().strip()))
edge={}
for i in range(N-1):
    u,v=map(int,sys.stdin.readline().split())
    if u not in edge:
        edge[u]=[]
    if v not in edge:
        edge[v]=[]
        
    edge[u].append(v)
    edge[v].append(u)
    
indoor=[]
total = 0
for i in range(len(A)):
    if A[i]==1:
        indoor.append(i+1)
        
     
def dfs():
    global total
    stack=[]
    
    for i in indoor:
        stack.append(i)
        visit=[False]*(N+1)
        visit[i]=True
        
        while stack:
            v=stack.pop()
            
            for j in edge.get(v,[]):
                if visit[j]==False:
                    if j in indoor:
                        visit[j]=True
                        total+=1
                    else :
                        visit[j]=True
                        stack.append(j)

dfs()
print(total)

    
    