import sys
from collections import deque

N= int(sys.stdin.readline())
M= int(sys.stdin.readline())

indegree=[0]*(N+1)
needs = [[0] * (N + 1) for _ in range(N + 1)]
list=[[] for _ in range(N + 1)]

for i in range(M):
    X,Y,K=map(int,sys.stdin.readline().split())  
    list[Y].append((X,K))
    indegree[X]+=1
q = deque() 
for i in range(1, N + 1):    
    if indegree[i] == 0:
        q.append(i)    
  
while q:
    now = q.popleft()
    for next, next_need in list[now]:
        if needs[now].count(0) == N + 1:
            needs[next][now] += next_need
        else:
            for i in range(1, N + 1):
                needs[next][i] += needs[now][i] * next_need    
        
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)
            
for i in range(len(needs[N])):
    if needs[N][i] > 0:
        print(i, needs[N][i])
        