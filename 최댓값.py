import sys

A=[]

for i in range(9):
    A.append(int(sys.stdin.readline()))  
   
maximum=A[0]
for i in range(9):
    if maximum<A[i]:
        maximum=A[i]

print(maximum)
print(A.index(maximum)+1)