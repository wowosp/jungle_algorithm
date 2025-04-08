import sys

N=int(sys.stdin.readline())

arr=[]
for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

arr.sort(key=lambda x:(x[1],x[0]))

solve=[]
for i in range(len(arr)):
    if len(solve)==0:
        temp=arr[i][1]
        solve.append(arr[i])
        continue 
    if temp<=arr[i][0] :
        temp=arr[i][1]
        solve.append(arr[i])
    else:
        continue 

print(len(solve))