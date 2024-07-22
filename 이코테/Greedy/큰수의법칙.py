n,m,k=map(int,input().split())

data = list(map(int, input().split()))

data.sort()

# print(data)
# print(data[-1],data[-2])

rpt = 0
ans = 0
for _ in range(m):

    if rpt==k:
        rpt=0
        ans+=data[-2]
        continue
    ans +=data[-1]
    rpt+=1

print(ans)