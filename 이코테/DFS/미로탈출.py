from collections import deque

n,m = map(int, input().split())

board=[]
for _ in range(n):
    board.append(list(map(int,input())))

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def is_valid(y,x):
    return 0<=y<n and 0<=x<m

q=deque()
q.append((0,0))
while len(q)>0:
    y,x = q.popleft()

    if (y,x) == (n-1,m-1):
        print(board[y][x])
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if not is_valid(ny,nx):
            continue

        if board[ny][nx]!=0:
            board[ny][nx]=board[y][x]+1
            q.append((ny,nx))