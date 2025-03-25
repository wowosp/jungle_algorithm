import sys

N, C= map(int, sys.stdin.readline().split())

A=[]
for i in range(N):
    A.append(int(sys.stdin.readline()))
    
A.sort()

def is_valid(arr,mid):
    count=1
    last=arr[0]
    
    for i in range(1,len(arr)):
        if arr[i]-last>=mid:
            count += 1
            last=arr[i]
            if count>=C:
                return True
        
    return False
    
def binary_search(arr):
    left, right = 1, max(arr)-min(arr) 
    best_answer = None  
    
    while left <= right:
        mid = (left + right) // 2  
        
        if is_valid(arr,mid):  
            best_answer = mid  
            left = mid + 1 
        else:
            right = mid - 1  
    
    return best_answer 

print(binary_search(A))