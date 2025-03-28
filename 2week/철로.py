import sys
import heapq

n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

d=int(sys.stdin.readline())

for i in range(len(arr)):
    if arr[i][0]<arr[i][1]:
        arr[i][0],arr[i][1]=arr[i][1],arr[i][0]

heapq.heapify(arr)

heap=[]
max_zone=0
while arr:
    start=arr[0][0]-d
    o, h = heapq.heappop(arr)
    heapq.heappush(heap, (h, o))
    if heap[0][0]<start:
        heapq.heappop(heap)
    if max_zone<len(heap):
        max_zone=len(heap)
        
print(max_zone)