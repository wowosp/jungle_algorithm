import sys

N, M = map(int, sys.stdin.readline().split())


def combination(n, m):
    result = []

    def backtrack(arr):
        if len(arr) == m:
            result.append(arr[:])
            return
        
        for i in range(1,n + 1):
            if i not in arr:
                arr.append(i)
                backtrack(arr)
                arr.pop()

    backtrack([])
    return result


result = combination(N, M)
for i in range(len(result)):
    print(*result[i])
