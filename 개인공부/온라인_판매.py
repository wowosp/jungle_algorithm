import sys

N, M = map(int, sys.stdin.readline().split())

pi=[]
for i in range(M):
    pi.append(int(sys.stdin.readline()))
    
pi.sort()
best_cost=pi[0]
if N >= M:
    max_cost = best_cost*N
else:
    max_cost = best_cost*M

for i in range(1,len(pi)):
    if len(pi)-i >= N:
        if pi[i]*N > max_cost:
            max_cost = pi[i]*N
            best_cost = pi[i]
    else:
        if pi[i]*(len(pi)-i) > max_cost:
            max_cost = pi[i]*(len(pi)-i)
            best_cost = pi[i]
            
print(best_cost, max_cost)      