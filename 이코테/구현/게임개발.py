n,m = map(int,input().split())

y,x,dir = map(int,input().split())

dx=[0,1,0,-1]
dy=[-1,0,1,0]

visit = [[0 for _ in range(m)] for _ in range(n)]
visit[y][x]=1

board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

def is_valid(ny,nx):
    return 0<=ny<n and 0<=nx<m

back = False
result = 0
while True:
    back = True
    for i in range(4,0,-1):
        dir = (dir+i)%4
        ny = y+dy[dir]
        nx = x+dx[dir]
        if is_valid(ny,nx) and not visit[ny][nx] and board[ny][nx]==0:
            visit[ny][nx]=1
            back =False
            result +=1
            y=ny
            x=nx
            break
    if back:
        if is_valid(y-1,x-1) and board[y-1][x-1]==0:
            y-=1
            x-=1
            result+=1
        else:
            break

print(result)