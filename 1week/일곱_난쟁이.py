import sys

dwarf=[]
for i in range(9):
    dwarf.append(int(sys.stdin.readline()))

dwarf.sort()

sum=0 
for i in dwarf:
    sum+=i
    
liar=sum-100

for i in range(9):
    for j in range(i + 1, 9):
        if dwarf[i]+dwarf[j]==liar:
            liar1, liar2 = dwarf[i], dwarf[j]
            dwarf.remove(liar1)
            dwarf.remove(liar2)           
            break
    else:
        continue
    break
                
for i in dwarf:
    print(i)