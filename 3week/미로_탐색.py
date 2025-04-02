import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().strip())))

def bfs(row, col):
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    queue.append((row, col))
    visited[row][col] = True
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    
    while queue:
        y, x = queue.popleft()
        
        if y == N-1 and x == M-1:
            return visited[y][x]
        
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and arr[ny][nx] != 0:
                visited[ny][nx] = visited[y][x] + 1 
                queue.append([ny,nx])
    return 

print(bfs(0,0))

    
    