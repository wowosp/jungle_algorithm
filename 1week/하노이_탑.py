import sys

N=int(sys.stdin.readline())

def hanoi_tower(n):
    if n==1:
        return 1
    else:
        return 1+2*hanoi_tower(n-1)
    
def how_hanoi_tower(n,x,y):
    if n>1:
        how_hanoi_tower(n-1,x,6-x-y)
        
    print(x,y)
    
    if n>1:
        how_hanoi_tower(n-1,6-x-y,y) 

print(hanoi_tower(N))

if N<=20:
    how_hanoi_tower(N,1,3)