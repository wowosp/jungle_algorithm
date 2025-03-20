import sys

N=int(sys.stdin.readline())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def combination(n):
    result=[]
    def dfs(idx,current):
        if len(current)==N//2:
            result.append(current[:])
            return
        
        for i in range(idx,n+1):
            current.append(i)
            dfs(i+1,current)
            current.pop()
            
    dfs(1,[])
    return result
        
teams=combination(N)
min_value = float('inf')


for team in teams:
    start_team=[]
    link_team=[]
    start_sum=0
    link_sum=0
    
    start_team=team
    
    for x in range(1,N+1):
        if x not in start_team:
            link_team.append(x)
    for i in start_team:
        for j in start_team:
            start_sum+=arr[i-1][j-1]
    for i in link_team:
        for j in link_team:
            link_sum+=arr[i-1][j-1]
    if abs(start_sum-link_sum)<min_value:
        min_value=abs(start_sum-link_sum)

print(min_value)