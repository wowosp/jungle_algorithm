import sys
import heapq

N=int(sys.stdin.readline())
heap=[]

for i in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))
sum=0   

for _ in range(N-1):
    temp=heapq.heappop(heap)+heapq.heappop(heap)
    sum+=temp
    heapq.heappush(heap, temp)

print(sum)