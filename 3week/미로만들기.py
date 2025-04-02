import sys
import heapq

N=int(sys.stdin.readline())
arr=[]
for i in range(N):
    row=list(map(int,sys.stdin.readline().strip()))
    inv_row=[1-i for i in row]
    arr.append(inv_row)

def dijkstra(arr,srow,scol,frow,fcol):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    heap = [(arr[srow][scol], srow, scol)]
    
    distances = [[float('inf')] * N for _ in range(N)]
    distances[srow][scol] = arr[srow][scol]
    
    while heap:
        cost, y, x = heapq.heappop(heap)
        
        if (y == frow and x == fcol):
            return cost
        
        if cost > distances[y][x]:
            continue
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            new_cost = cost + arr[ny][nx]
            
            if new_cost < distances[ny][nx]:
                distances[ny][nx] = new_cost
                heapq.heappush(heap, (new_cost, ny, nx))
    
    return -1 

result = dijkstra(arr,0,0,N-1,N-1)
print(result)