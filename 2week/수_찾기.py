import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
B=list(map(int,sys.stdin.readline().split()))

A.sort()

def binary_find(arr,n,left,right):
    
    pivot=(left+right)//2
    if arr[pivot]==n:
        print(1)
        return
    
    if left>right:
        print(0)
        return
    
    elif n>arr[pivot]:
        binary_find(arr,n,pivot+1,right)
        
    elif n<arr[pivot]:
        binary_find(arr,n,left,pivot-1)
        
        
for j in B:
    binary_find(A,j,0,N-1)