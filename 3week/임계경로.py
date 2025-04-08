import sys
from collections import deque

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

adj={}
indegree=[0]*(n+1)
arr=[[0, 0] for _ in range(n + 1)]
for i in range(m):
    u,v,w=map(int,sys.stdin.readline().split())
    if u not in adj:
        adj[u]=[]
        
    adj[u].append((w,v))
    indegree[v]+=1

start, end = map(int,sys.stdin.readline().split())

arr[start]=[0,1]

def sol(start):
    q=deque()
    q.append(start)
    
    while q:
        node=q.popleft()
        
        for nw, next in adj.get(node,[]):
            indegree[next] -= 1
            new_weight = arr[node][0] + nw
            new_levle=arr[node][1]+1
            
            if new_weight==arr[next][0]:
                arr[next][1]+=arr[node][1]-1
    
            elif new_weight>arr[next][0]:
                arr[next][0]=new_weight
                arr[next][1]=new_levle
                
            if indegree[next] == 0:
                q.append(next)
        
sol(start)               
print(arr[end][0])
print(arr[end][1])      
        
        

