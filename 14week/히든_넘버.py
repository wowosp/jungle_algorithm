import sys

N = int(sys.stdin.readline())
num = str(sys.stdin.readline())

solve = 0 
temp = 0

for i in range(N):
    if (num[i] == '0' or num[i] =='1' or num[i] =='2' or num[i] =='3' or num[i] =='4' or num[i] =='5' or num[i] =='6' or num[i] =='7' or num[i] =='8' or num[i] =='9'):
        if temp != 0:
            temp = temp*10 + int(num[i])
        else:
            temp = int(num[i])
            
    else:
        solve += temp
        temp = 0
        
if temp!=0:
    solve += temp
    
    
print(solve)      