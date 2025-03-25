import sys

N, M = map(int,sys.stdin.readline().split())

trees=list(map(int,sys.stdin.readline().split()))
        
def sum_trees(arr,target):
    sum=0
    for i in arr:
        if i>target:
            sum+=i-target
    return sum

def binary_search(arr):
    global max_length
    left, right = 0, max_value
    
    while left <= right:
        mid = (left + right) // 2
        
        if sum_trees(arr,mid)>=M:
            max_length=mid   
            left = mid + 1
        else:  
            right = mid - 1
    
    return max_length




        
trees.sort()        
max_value=max(trees)
max_length=0


binary_search(trees)
    
print(max_length)