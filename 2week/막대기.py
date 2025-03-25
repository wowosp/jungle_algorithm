import sys

N=int(sys.stdin.readline())
arr=[]

for i in range(N):
    arr.append(int(sys.stdin.readline()))
    
frist=arr.pop()
count=1

while arr:
    temp=arr.pop()
    if temp>frist:
        frist=temp
        count+=1
        
print(count)