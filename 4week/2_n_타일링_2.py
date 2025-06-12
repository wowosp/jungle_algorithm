import sys

n=int(sys.stdin.readline())


if n==0:
    print(0)

elif n==1:
    print(1)
    
else:
    arr=[0]*n
    arr[0]=1
    arr[1]=3

    for i in range(2,n):
        arr[i]=arr[i-1]%10007+(arr[i-2]*2)%10007
        
    print(arr[n-1]%10007)

