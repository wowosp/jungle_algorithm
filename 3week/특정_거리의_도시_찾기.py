import sys 
import heapq

N,M,K,X=map(int,sys.stdin.readline().split())
edge={}

for i in range(M):
    s,t=map(int,sys.stdin.readline().split())
    
    if s not in edge:
        edge[s]=[]
    
    edge[s].append((1,t))
    

def dijkstra(graph, start):
    result=[float('inf')]*(N+1)
    result[start]=0
    
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        
        if result[u]<current_dist:
            continue
        
        for weight,v in graph.get(u, []):
            new_dist = result[u] + weight
            
            if new_dist < result[v]:
                result[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
                
    return result

result=dijkstra(edge, X)

for i in range(len(result)):
    if result[i]==K:
        print(i)
if K not in result:
    print(-1)