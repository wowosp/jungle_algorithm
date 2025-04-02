import sys

N=int(sys.stdin.readline())

arr=list(map(int,sys.stdin.readline().split()))

operator=list(map(int,sys.stdin.readline().split()))

maximum = float('-inf')
minimum = float('inf')

def find_solve(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    
    if depth==N:
        maximum=max(total,maximum)
        minimum=min(total,minimum)
        return
    
    if plus:
        find_solve(depth+1, total+arr[depth], plus-1, minus, multiply, divide)
    if minus:
        find_solve(depth+1, total-arr[depth], plus, minus-1, multiply, divide)
    if multiply:
        find_solve(depth+1, total*arr[depth], plus, minus, multiply-1, divide)
    if divide:
        find_solve(depth+1, int(total/arr[depth]), plus, minus, multiply, divide-1)
        
find_solve(1, arr[0], operator[0], operator[1], operator[2], operator[3])
print(maximum)
print(minimum)