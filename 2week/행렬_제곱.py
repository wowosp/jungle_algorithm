import sys

N,B=map(int,sys.stdin.readline().split())
C=1000
matrix=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]


def matrix_power(arr,exponent):
    if exponent == 0: 
        return [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    tmp = matrix_power(arr,exponent//2)
    if exponent % 2: 
        return matrix_product(arr,matrix_product(tmp,tmp))
    else: 
        return matrix_product(tmp,tmp)
    

def matrix_product(arr1,arr2):
    product=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                product[i][j]=(product[i][j]+arr1[i][k]*arr2[k][j])%C
                
    return product

result=matrix_power(matrix,B)
for i in range(N):
    print(*result[i])