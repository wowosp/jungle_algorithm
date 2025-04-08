import sys

arr=list(sys.stdin.readline().strip().split('-'))
print(arr)

start=list(map(int,arr[0].split('+')))
sum=0
for i in range(len(start)):
    sum+=start[i]

for i in range(1,len(arr)):
    minus=0
    tmep=list(map(int,arr[i].split('+')))
    for j in range(len(tmep)):
        minus+=tmep[j]
    sum-=minus    
    
print(sum)