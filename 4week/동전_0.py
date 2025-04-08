import sys

N,K=map(int,sys.stdin.readline().split())

arr=[]
for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=1)
sum=K
count=0
for i in arr:
    count+=sum//i
    sum=sum%i
        
print(count)