from collections import deque

n,m = map(int,input().split())

# dp = [[1e9]*(n+1) for _ in range(n+1)]
board=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,input().split())
    board[a].append((b,c))
    board[b].append((a,c))


#
# for k in range(n+1):
#     for i in range(n+1):
#         for j,_ in board[i]:
#             dp[i][j]=min(dp[i][k] + dp[k][j], dp[i][j])
#


def bfs(start,end):
    q=deque()
    q.append((start,0))
    visit=[False]*(n+1)
    visit[start] = True

    while q:
        now,cost = q.popleft()
        for nxt, c in board[now]:
            if nxt == end:
                return cost+c
            if not visit[nxt]:
                visit[nxt]=True
                q.append((nxt, cost+c))

for _ in range(m):
    start, end = map(int,input().split())
    print(bfs(start,end))
    # print(dp[start][end])