import sys

N=int(sys.stdin.readline())

def counting_sort(arr):
    max_val=max(arr)
    min_val=min(arr)
    range_size=max_val-min_val+1
    
    count=[0]*range_size
    output=[0]*len(arr)
    
    for i in arr:
        count[i-min_val]+=1
        
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        
    for i in reversed(a):
        count[i-min_val]-=1
        output[count[i-min_val]]=i
    
    for i in range(len(arr)):
        arr[i]=output[i]

a=[]

for i in range(N):
    a.append(int(sys.stdin.readline()))
    
counting_sort(a)

for i in a:
    print(i)
    
    