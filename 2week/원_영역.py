import sys

N=int(sys.stdin.readline())
stack=[]
count=1

circle=[]
for i in range(N):
    x,r=map(int,sys.stdin.readline().split())
    circle.append(["L", x-r])
    circle.append(["R", x+r])
    
circle.sort(key=lambda p: (-p[1], p[0]), reverse=True)

for i in circle:
    if i[0] == "L":
        stack.append(i)
    else:
        cum_width = 0

        while stack:
            prev = stack.pop()

            if prev[0] == "L":
                width = i[1] - prev[1]

                if width == cum_width:
                    count += 2
                else:
                    count += 1

                stack.append(["C", width]) 
                break

            elif prev[0] == "C":
                cum_width += prev[1]
    
print(count)