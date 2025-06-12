import sys

A = int(sys.stdin.readline())
i = 2
while (A != 1):
    if (A % i == 0):
        print(i)
        A = A/i
    else:
        i += 1
        

         