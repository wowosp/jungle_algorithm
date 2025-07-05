import sys

N=int(sys.stdin.readline())
i=0
solve=0
while(N != solve and i <= N):
    temp=str(i)
    solve=i
    for j in range(len(temp)):
        solve += int(temp[j])
    i+=1

if (N == solve):
    print(i-1)
else:
    print(0)