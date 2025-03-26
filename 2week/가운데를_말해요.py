import sys
import heapq

N=int(sys.stdin.readline())

left=[]
right=[]

for i in range(N):
    if len(left)==len(right):
        heapq.heappush(left, -int(sys.stdin.readline()))
    else :
        heapq.heappush(right, int(sys.stdin.readline()))
    
    if left and right:    
        if -left[0]>right[0]:
            left_value=heapq.heappop(left)
            right_value=heapq.heappop(right)
            heapq.heappush(left,-right_value)
            heapq.heappush(right,-left_value)
                
    print(-left[0])