import sys

M,N,L=map(int,sys.stdin.readline().split())

hunter=list(map(int,sys.stdin.readline().split()))
hunter.sort()
animal=[]
for i in range(N):
    animal.append(list(map(int,sys.stdin.readline().split())))

result = 0

for a, b in animal:
    lt = 0 
    rt = len(hunter) - 1
    forward_range = a + b - L 
    behind_range = a - b + L 

    while lt <= rt:
        mid = (lt + rt) // 2
    
        if forward_range <= hunter[mid] <= behind_range:
            result += 1
            break
        elif forward_range > hunter[mid]:
            lt = mid + 1
        elif behind_range < hunter[mid]:
            rt = mid - 1

print(result)