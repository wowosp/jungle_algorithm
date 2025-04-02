import sys

K=int(sys.stdin.readline())

def binary_graph(V, edge):
    check=[-1]*(V+1)
    stack=[]
    
    for start in edge.keys():  
        if check[start] != -1:  
            continue
        
        stack.append(start)
        check[start] = 1
    
        while stack:
            v=stack.pop()
        
            for i in edge.get(v,[]):
                if check[v]==check[i]:
                    print('NO')
                    return 
                if check[i] == -1:
                    check[i] = 0 if check[v]==1 else 1
                    stack.append(i)
                
    print('YES')
                 
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    edge = {}
    
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        if u not in edge:
            edge[u]=[]
        if v not in edge:
            edge[v]=[]
        edge[v].append(u)
        edge[u].append(v)
        
    binary_graph(V, edge)