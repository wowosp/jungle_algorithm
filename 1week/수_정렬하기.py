import sys

N=int(sys.stdin.readline())

a=[]
for i in range(N):
    a.append(int(sys.stdin.readline()))

def buble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

buble_sort(a)

prev=None
for i in a:
    if i!=prev:
        print(i)
        prev=i