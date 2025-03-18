import sys

def qsort(arr):
    if len(arr)<=1:
        return arr
    
    pivot=arr.pop()
    left=[x for x in arr if compare(pivot, x)]
    right=[x for x in arr if compare(x, pivot)]
    return qsort(left)+[pivot]+qsort(right)
    
def compare(x1,x2):
    if len(x1) != len(x2):
        return len(x2)<len(x1)
    else:
        return x2<x1

    
N=int(sys.stdin.readline())


a=list(set(line.strip() for line in sys.stdin.readlines()))


for i in qsort(a):
    print(i)