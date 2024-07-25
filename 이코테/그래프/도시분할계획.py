import heapq

n,m = map(int,input().split())

road = []
for i in range(n+1):
    road.append(i)

q=[]


for _ in range(m):
    a,b,c = map(int,input().split())
    heapq.heappush(q,(c,a,b))

def parent(lst, a):
    if lst[a]!=a:
        lst[a]=parent(lst,lst[a])
    return lst[a]

def union(lst, a,b):
    a = parent(lst,a)
    b = parent(lst,b)

    if a<b:
        lst[b]=a
    else:
        lst[a]=b
    if a == b:
        return False
    else:
        return True

result = 0
max_cost = 0
while q:
    cost,start,end = heapq.heappop(q)
    if union(road,start,end):
        result += cost
        max_cost = max(max_cost, cost)
print(result- max_cost)