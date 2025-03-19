import sys

N=int(sys.stdin.readline())

W=[]
for i in range(N):
    W.append(list(map(int,sys.stdin.readline().split())))

def TSP(arr):
    visited=[0]*N
    min_cost = float('inf')

    def backtrack(current,count,cost):
        nonlocal min_cost
        if count == N:
            if arr[current][0] != 0:
                total_cost=cost+arr[current][0]
                if min_cost>total_cost:
                    min_cost=total_cost
            return
        
        for i in range(N):
            if visited[i] or arr[current][i] == 0:
                continue
            visited[i]=1
            
            backtrack(i,count+1,cost + arr[current][i])
            
            visited[i]=0
            
    visited[0] = True
    backtrack(0, 1, 0)

    return min_cost  

print(TSP(W))