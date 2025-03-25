import sys

def solution(left, right):
    global heights

    if left == right:
        return heights[left]

    mid = (left + right) // 2

    area = max(solution(left, mid), solution(mid + 1, right))

    lmid = mid
    rmid = mid + 1
    height = min(heights[lmid], heights[rmid])

    area = max(area, height * 2)

    while left < lmid or rmid < right:
        if rmid < right and (lmid == left or heights[lmid - 1] < heights[rmid + 1]):
            rmid += 1
            height = min(height, heights[rmid])
        else:
            lmid -= 1
            height = min(height, heights[lmid])

        area = max(area, height * (rmid - lmid + 1))

    return area

while True:
    N, *heights = map(int, sys.stdin.readline().split())
    if N == 0:
        break
    print(solution(0, N-1))
    
