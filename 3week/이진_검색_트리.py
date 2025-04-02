import sys
sys.setrecursionlimit(10**9)

tree=[]
while True:
    try:
        tree.append(int(sys.stdin.readline()))
    
    except:
        break
    
def solve(arr):
    if len(arr)==0:
        return
    
    tempL,tempR=[],[]
    
    mid=arr[0]
    
    for i in range(1,len(arr)):
        if arr[i]>mid:
            tempL=arr[1:i]
            tempR=arr[i:]
            break
    else:
        tempL=arr[1:]
        
    solve(tempL)
    solve(tempR)
    print(mid)
    
solve(tree)

