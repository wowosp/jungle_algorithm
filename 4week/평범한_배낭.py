import sys

N, K= map(int,sys.stdin.readline().split())

arr=[]
for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
    
dp=[[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if arr[i-1][0]<=j:
            dp[i][j]=max(arr[i-1][1]+dp[i-1][j-arr[i-1][0]],dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]
            
print(dp[N][K])