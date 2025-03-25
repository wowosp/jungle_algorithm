import sys

T=int(sys.stdin.readline())


for i in range(T):
    count_left=0
    count_right=0
    N=list(sys.stdin.readline().strip('\n'))

    while N:
        temp=N.pop()
        if temp=='(':
            count_left+=1
        else :
            count_right+=1
        
        if count_left>count_right:
            print('NO')
            break
        
    else:
        if count_left!=count_right:
            print('NO')
        else:
            print('YES')
