board = []

n,m=map(int,input().split())

for _ in range(n):
    data = input()
    lst=[]
    for i in data:
        lst.append(int(i))
    board.append(lst)



# visit = [[0 for _ in range(5)] for _ in range(4)]

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def is_valid(y,x):
    return 0<=y<n and 0<=x<m

def dfs(y,x):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if not is_valid(ny,nx):
            continue
        if board[ny][nx]==0:
            board[ny][nx]=1
            dfs(ny,nx)

if __name__ == '__main__':
    result = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                board[i][j]=1
                dfs(i,j)
                result+=1

    print(result)


