import sys

w, h= map(int,sys.stdin.readline().split())
N=int(sys.stdin.readline())
X=[0,w]
Y=[0,h]
LenX=[]
LenY=[]

for i in range(N):
    how, where= map(int,sys.stdin.readline().split())
    if how == 1:
        X.append(where)
    else:
        Y.append(where)
    
X.sort()
Y.sort()

for i in range(len(X)-1):
    LenX.append(X[i+1]-X[i])
for i in range(len(Y)-1):
    LenY.append(Y[i+1]-Y[i])

print(max(LenX)*max(LenY))