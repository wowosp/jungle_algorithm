import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

apple = set()
for _ in range(K):
    row, col = map(int, sys.stdin.readline().split())
    apple.add((row, col))  

L = int(sys.stdin.readline())
commands = []
for _ in range(L):
    t, d = sys.stdin.readline().split()
    commands.append((int(t), d))

snake = deque([(1, 1)]) 
direction = 0
time = 0
cmd_idx = 0

while True:
    if cmd_idx < L and time == commands[cmd_idx][0]:
        if commands[cmd_idx][1] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        cmd_idx += 1

    if direction == 0:
        new_head_row, new_head_col = snake[-1][0], snake[-1][1] + 1
    elif direction == 1:
        new_head_row, new_head_col = snake[-1][0] + 1, snake[-1][1]
    elif direction == 2:
        new_head_row, new_head_col = snake[-1][0], snake[-1][1] - 1
    else:
        new_head_row, new_head_col = snake[-1][0] - 1, snake[-1][1]
    

    if new_head_row < 1 or new_head_row > N or new_head_col < 1 or new_head_col > N:
        print(time + 1)
        sys.exit()
    if (new_head_row, new_head_col) in snake:
        print(time + 1)
        sys.exit()
    
  
    if (new_head_row, new_head_col) in apple:
        apple.remove((new_head_row, new_head_col))
    else:
        snake.popleft()
    
    snake.append((new_head_row, new_head_col))
    time += 1

    
    
    