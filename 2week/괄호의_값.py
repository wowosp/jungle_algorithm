import sys

arr = list(sys.stdin.readline().strip())

stack = []
solve = 0
temp = 1
prev = ''  

for i in arr:
    if i == '(':
        stack.append(i)
        temp *= 2
        prev = i
    elif i == '[':
        stack.append(i)
        temp *= 3
        prev = i
    elif i == ')':
        if not stack or stack[-1] != '(':
            print(0)
            exit()
        if prev == '(':
            solve += temp
        stack.pop()
        temp //= 2
        prev = i
    elif i == ']':
        if not stack or stack[-1] != '[':
            print(0)
            exit()
        if prev == '[':
            solve += temp
        stack.pop()
        temp //= 3
        prev = i
    else:
        print(0)
        exit()

if stack:
    print(0)
else:
    print(solve)