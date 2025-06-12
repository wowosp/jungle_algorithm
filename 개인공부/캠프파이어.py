import sys

N=int(sys.stdin.readline())

E=int(sys.stdin.readline())


for i in range(E):
    arr=list(map(int,sys.stdin.readline().split()))
    
    k=arr[0]
    del arr[0]
    temp=set(arr)
    
    if 1 in temp:
        solve |= temp
            
    else:
        if (solve & temp) == {1} or (solve & temp) == set():
            continue
                
        else:
            solve = solve | temp

                       
sorted_solve=sorted(solve)

for i in range(len(sorted_solve)):
    print(sorted_solve[i])