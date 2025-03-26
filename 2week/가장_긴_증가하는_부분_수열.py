import sys

N=int(sys.stdin.readline())

A=list(map(int,sys.stdin.readline().split()))

def binary_search(target,arr):
    start,end = 0,len(arr)-1
    while start < end:
        mid = (start + end) // 2 
        if arr[mid] == target:
            return mid
        elif arr[mid-1] < target < arr[mid]: 
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start 

def sol(a,n):
    arr = [a[0]] 
    for i in range(1,n):
        target = a[i]
        if arr[-1] < target: 
            arr.append(target)
        else:
            idx = binary_search(target,arr)
            arr[idx] = target

    return len(arr) 

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