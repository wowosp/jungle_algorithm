import sys

T=int(sys.stdin.readline())

for _ in range(T):
    N=int(sys.stdin.readline())
    coin=list(map(int,sys.stdin.readline().split()))
    total=int(sys.stdin.readline())
    
    dp=[0]*(total+1)
    dp[0]=1
    
    for i in range(N):
        for j in range(1,total+1):
            if j-coin[i]>=0:
                dp[j]+=dp[j-coin[i]]

    print(dp[total])