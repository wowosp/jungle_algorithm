import sys

T=int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr=[]
    S=[]
    E=[]
    
    for _ in range(N):
        arr.append(list(map(int,sys.stdin.readline().split())))
    arr.sort()
    for i in arr:
        S.append(i)
        
    arr.sort(key=lambda x:x[1])
    
    for i in arr:
        E.append(i)
    
    solve=[]
  
    S_max=S[0][1]
    E_max=E[0][0]

    for i in range(N):
        if S[i][0]>E_max:
            continue
        
        if S[i][1]<=S_max:
            solve.append(S[i])
            S_max=S[i][1]
            
        if E[i][1]>=S_max:
            continue  
          
        if E[i][0]<E_max:
            solve.append(E[i])
            E_max=E[i][0]
    
    print(len(solve))