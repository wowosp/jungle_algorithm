import sys

solve = list(sys.stdin.readline().strip('\n'))
N=int(sys.stdin.readline())
temp=[]

for i in range(N):
    input = sys.stdin.readline()
    if (input[0]=='P'):
        solve.append(input[2])
    elif (input[0]=='L'):
        if len(solve)!=0:
            temp.append(solve.pop())
    elif (input[0]=='D'):
        if len(temp)!=0:
            solve.append(temp.pop())
    else:
        if len(solve)!=0:
            solve.pop()

while(temp):
    solve.append(temp.pop())

print(*solve, sep='')
