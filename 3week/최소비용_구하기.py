import sys
import heapq

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

graph={}
for i in range(M):
    u, v, weight = map(int,sys.stdin.readline().split())
    
    if u not in graph:
        graph[u]=[]
        
    graph[u].append((weight,v))
    
start,end=map(int,sys.stdin.readline().split())

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

result=dijkstra(graph, start)

print(result[end])