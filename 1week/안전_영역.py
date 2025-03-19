import sys
sys.setrecursionlimit(10**6)

N=int(sys.stdin.readline())

W=[]
for i in range(N):
    W.append(list(map(int,sys.stdin.readline().split())))

maxvalue=max(max(row) for row in W)
minvalue=min(min(row) for row in W)

def backtrack(arr,row,col): 
    if row < 0 or row >= N or col < 0 or col >= N or arr[row][col] == 1:
        return
        
    arr[row][col]=1
    backtrack(arr,row+1,col)
    backtrack(arr,row-1,col)
    backtrack(arr,row,col+1)
    backtrack(arr,row,col-1)
        
result = 0
    
for k in range(minvalue-1,maxvalue): 
    check=[[0]*N for _ in range(N)] 
      
    for i in range(N):
        for j in range(N):
            if W[i][j] <= k:
                check[i][j]=1
    
    safe_area=0
    
    for i in range(N):
        for j in range(N):
            if check[i][j] == 0: 
                backtrack(check,i,j)
                safe_area += 1            
    
    result = max(result, safe_area)

print(result)                    