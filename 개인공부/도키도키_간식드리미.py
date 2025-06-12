import sys

N=int(sys.stdin.readline())

arr=list(map(int,sys.stdin.readline().split()))

num=1
temp=[]

for i in range(len(arr)):
    if arr[i] != num:
        temp.append(arr[i])
    else:
        num+=1
        if len(temp) != 0:
            while True:
                if len(temp) != 0:
                    if temp[-1] == num:
                        temp.pop()
                        num+=1
                    else:
                        break
                else:
                    break        
                

for _ in range(len(temp)):
    if temp.pop() != num:
        print("Sad")
        break
    else:
        num+=1
        
if len(temp) ==0:
    print("Nice")