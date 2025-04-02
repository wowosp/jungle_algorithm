# import sys

# N=int(sys.stdin.readline())
# tree={}
# for i in range(N):
#     key, left, right = map(str, sys.stdin.readline().split())
#     tree[key]=[left,right]
    
# def dfs_preorder(node):
#     if node == '.' or not node: 
#         return
    
#     print(node, end='')         
#     dfs_preorder(tree[node][0]) 
#     dfs_preorder(tree[node][1])  
    
# def dfs_inorder(node):
#     if node == '.' or not node: 
#         return
            
#     dfs_inorder(tree[node][0])
#     print(node, end='')  
#     dfs_inorder(tree[node][1])        

# def dfs_postorder(node):
#     if node == '.' or not node: 
#         return
            
#     dfs_postorder(tree[node][0])
#     dfs_postorder(tree[node][1]) 
#     print(node, end='') 

# visited={key: False for key in tree.keys()}
# dfs_preorder('A')
# print()
# dfs_inorder('A')   
# print() 
# dfs_postorder('A')    


import sys

# 트리 구성
N = int(sys.stdin.readline())
tree = {}
for _ in range(N):
    key, left, right = sys.stdin.readline().split()
    tree[key] = [left, right]

# 전위 순회 (Pre-order)
def preorder_stack(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node == '.':
            continue
        print(node, end='')
        stack.append(tree[node][1])  # 오른쪽 먼저 추가
        stack.append(tree[node][0])  # 왼쪽 나중에 추가

# 중위 순회 (In-order)
def inorder_stack(root):
    stack = []
    current = root
    while stack or current != '.':
        # 왼쪽 끝까지 이동
        while current != '.':
            stack.append(current)
            current = tree[current][0]
        # 스택에서 꺼내 출력
        current = stack.pop()
        print(current, end='')
        # 오른쪽 자식으로 이동
        current = tree[current][1]

# 후위 순회 (Post-order)
def postorder_stack(root):
    stack = [(root, False)]  # (노드, 방문여부)
    while stack:
        node, visited = stack.pop()
        if node == '.':
            continue
        if visited:
            print(node, end='')
        else:
            stack.append((node, True))          # 현재 노드 재방문용
            stack.append((tree[node][1], False)) # 오른쪽 자식
            stack.append((tree[node][0], False)) # 왼쪽 자식

# 실행
preorder_stack('A')
print()
inorder_stack('A')
print()
postorder_stack('A')