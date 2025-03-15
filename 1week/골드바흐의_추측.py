import sys
import math

def prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    A = int(N / 2)
    B = int(N / 2)
    
    while True:
        if prime_number(A) == 1 and prime_number(B)==1 and A+B == N:
            print(A,B)
            break
        if prime_number(A) == 0 or prime_number(B)==0 or A+B == N:
            if A%2==0:
                A-=1
                B+=1
            else :
                A-=2
                B+=2