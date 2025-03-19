import sys

x, y, w, h= map(int, sys.stdin.readline().split())

left=x
right=w-x
top=h-y
bottom=y

minmum=left
if minmum>right:
    minmum=right
if minmum>top:
    minmum=top
if minmum>bottom:
    minmum=bottom
    
print(minmum)