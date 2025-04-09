import sys

arr1=list(sys.stdin.readline().strip())
arr2=list(sys.stdin.readline().strip())

col=['']+arr1
row=['']+arr2

dp=[[0]*len(col) for _ in range(len(row))]

for i in range(len(row)):
    dp[i][0]=i

for i in range(len(col)):
    dp[0][i]=i

for i in range(1,len(row)):
    for j in range(1,len(col)):
        if row[i]==col[j]:
            dp[i][j]=dp[i-1][j-1] 
        else:
            dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
            
print(dp[len(row)-1][len(col)-1])