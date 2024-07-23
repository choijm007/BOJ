import heapq

n,m,start=map(int,input().split())


graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
INF=int(1e9)
distance = [INF]*(n+1)

def dij(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))

dij(start)
cnt = -1
result =0
for i in distance:
    if i!=INF:
        cnt+=1
        result = max(result,i)

print(distance)
print(cnt, result)
