import sys

N,K=map(int,sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().strip()))

stack=[]

for i in arr:
    while stack and stack[-1] < i and K > 0:
        stack.pop()
        K -= 1
    stack.append(i)
if K > 0:
    print(''.join(map(str, stack[:-K])))
else:
    print(''.join(map(str, stack)))