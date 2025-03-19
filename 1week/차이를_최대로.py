import sys

N=int(sys.stdin.readline())

A=list(map(int,sys.stdin.readline().split()))

def permute(arr):
    result=[]
    visited=[0]*N
    
    def backtrack(temp):
        if len(temp) == len(arr):
            result.append(temp[:])
            return

        for i in range(len(arr)):
            if visited[i]:
                continue
            visited[i]=1
            temp.append(arr[i])
            backtrack(temp)
            temp.pop()
            visited[i]=0
            
    backtrack([])
    return result

def max_diff(arrs):
    max_value=0
    
    for arr in arrs:
        temp_sum=0 
        for i in range(len(arr)-1):
            temp_sum+=abs(arr[i]-arr[i+1])
        if max_value<temp_sum:
            max_value=temp_sum
            
    return max_value
        
    
print(max_diff(permute(A)))
