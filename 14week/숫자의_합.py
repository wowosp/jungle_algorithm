import sys

N = int(sys.stdin.readline())

# num = int(sys.stdin.readline())
# i=1
# solve = 0

# while (i != N+1):
#     solve += ((num % (10**i)) - (num % 10**(i-1)))/(10**(i-1))
#     i += 1
# print(int(solve)) 
    
S = sys.stdin.readline()
solve = 0
for i in range(N):
    solve += int(S[i])
    
print(solve)
