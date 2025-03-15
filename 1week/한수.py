import sys

N=int(sys.stdin.readline())

count=0
if N<100:
    print(N)
else:
    for i in range(1,N+1):
        if i<100:
            count+=1
        else:
            a=(i//100)
            b=(i%100//10)
            c=(i%10)
            if a-b == b-c:
                count+=1
    print(count)