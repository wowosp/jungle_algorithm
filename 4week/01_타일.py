import sys

N=int(sys.stdin.readline())
dp = [0] * (N + 1)
dp[0]=1
dp[1]=2

for i in range(2,N+1):
    dp[i]=dp[i-2]%15746+dp[i-1]%15746
    
print(dp[N-1]%15746)