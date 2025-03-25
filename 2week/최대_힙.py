import sys

N=int(sys.stdin.readline())
A=[]

def heapify(arr, n, i):
    largest = i       
    left = 2 * i + 1  
    right = 2 * i + 2 

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
def heapify_up(arr,i):
    if i<=0:
        return
    parent=(i-1)//2
    if arr[parent]<arr[i]:
        arr[i],arr[parent]=arr[parent],arr[i]
        heapify_up(arr,parent)

for i in range(N):
    x=int(sys.stdin.readline())
    if x == 0:
        if len(A)==0:
            print(0)
        else:
            A[0],A[len(A)-1]=A[len(A)-1],A[0]
            print(A.pop())
            heapify(A, len(A), 0)
            
    else :
        A.append(x)
        heapify_up(A,len(A)-1)
        
        


        





# import sys
# import heapq

# N=int(sys.stdin.readline())
# A=[]

# for i in range(N):
#     x=int(sys.stdin.readline())
#     if x == 0:
#         if len(A)==0:
#             print(0)
#         else:
#             print(-heapq.heappop(A))
           
#     else :
#         heapq.heappush(A, -x)