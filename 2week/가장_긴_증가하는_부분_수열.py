import sys

N=int(sys.stdin.readline())

A=list(map(int,sys.stdin.readline().split()))

def binary_search(target,lis):
    start,end = 0,len(lis)-1
    while start < end:
        mid = (start + end) // 2 
        if lis[mid] == target:
            return mid
        elif lis[mid-1] < target < lis[mid]: 
            return mid
        elif target < lis[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start 

def sol(a,n):
    lis = [a[0]] 
    for i in range(1,n):
        target = a[i]
        if lis[-1] < target: 
            lis.append(target)
        else:
            idx = binary_search(target,lis)
            lis[idx] = target

    return len(lis) 

print(sol(A,N))

# import sys

# N=int(sys.stdin.readline())

# A=list(map(int,sys.stdin.readline().split()))

# def max_length(arr):
#     if not arr:
#         return 0
    
#     dp = [1] * len(arr) 
    
#     for i in range(1, len(arr)):
#         for j in range(i):
#             if arr[i] > arr[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)
                
#     return max(dp)

# print(max_length(A))