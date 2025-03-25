import sys

N= int(sys.stdin.readline())

A=list(map(int,sys.stdin.readline().split()))
    
A.sort()

def two_solution(arr):
    left,right=0,len(arr)-1
    solve=float('inf')
    answer = (0, 0)
    
    while left<right:
        temp=arr[left]+arr[right]
        
        
        if abs(solve)>abs(temp):
            solve=temp
            answer = (arr[left], arr[right])
        
        if temp>0:
            right-=1
        elif temp<0:
            left+=1
        else:
            print(arr[left], arr[right])
            break
        
    print(answer[0], answer[1])        
        
    
two_solution(A)