import sys


arr1=list(sys.stdin.readline().strip())
arr2=list(sys.stdin.readline().strip())
M=len(arr2)
N=len(arr1)

dp=[[0 for _ in range(len(arr1)+1)] for _ in range(len(arr2)+1)]

for i in range(1,len(arr2)+1):
    for j in range(1,len(arr1)+1):
        if arr2[i-1]==arr1[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            
print(dp[M][N])
     