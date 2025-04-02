import sys
from collections import deque

M,N,H=map(int,sys.stdin.readline().split())

tomatos = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
base_tomatos = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatos[i][j][k] == 1:
                base_tomatos.append((i, j, k, 0))
                
q = deque(base_tomatos)

while q:
    x, y, z, cnt = q.popleft()
    
    visited[x][y][z] = 1

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and tomatos[nx][ny][nz] == 0 and visited[nx][ny][nz] != 1:
            q.append((nx, ny, nz, cnt+1))
            visited[nx][ny][nz] = 1
            tomatos[nx][ny][nz] = 1
            

break_flag = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatos[i][j][k] == 0:
                print(-1)
                break_flag = True
                break
            
        if break_flag:
            break
        
    if break_flag:
        break
if not break_flag :
    print(cnt)
            