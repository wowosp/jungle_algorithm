import sys

N,K=map(int,sys.stdin.readline().split())

arr=[]
result=[]
front=0

for i in range(1,N+1):
    arr.append(i)

while arr:
    front=(front+K-1)%len(arr)
    result.append(arr.pop(front))

print(f"<"+", ".join(map(str, result))+">")
        
        
        
        
        
# import sys

# N, K = map(int, sys.stdin.readline().split())

# arr = list(range(1, N + 1))  # 1부터 N까지의 숫자 리스트
# visited = [False] * N  # 삭제 여부를 체크하는 리스트
# result = []

# front = 0  # 현재 위치
# count = 0  # 방문한 노드 개수

# while count < N:
#     step = 0  # K번째를 찾기 위한 스텝 카운트

#     while step < K:  # K번째 살아있는 원소를 찾음
#         if not visited[front]:  # 아직 제거되지 않은 경우
#             step += 1
#         if step < K:  # K번째 전이면 다음 인덱스로 이동
#             front = (front + 1) % N

#     result.append(arr[front])  # 결과 리스트에 추가
#     visited[front] = True  # 해당 요소 삭제 표시
#     count += 1  # 제거한 개수 증가

# print(f"<" + ", ".join(map(str, result)) + ">")
    

    

