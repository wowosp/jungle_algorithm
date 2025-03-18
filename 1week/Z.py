import sys

N, r, c = map(int,sys.stdin.readline().split())
route=0
def Z(n,row,col):
    global route
    
    if n==0:
        return
    
    half=2**(n-1)
    
    if col<half and row<half:
        route+=0
        Z(n-1,row,col)
        
    elif col>=half and row<half:
        route+=half*half
        Z(n-1,row,col-half)
        
    elif col<half and row>=half:
        route+=2*half*half
        Z(n-1,row-half,col)
        
    elif col>=half and row>=half:
        route+=3*half*half
        Z(n-1,row-half,col-half)

Z(N, r, c)

print(route) 