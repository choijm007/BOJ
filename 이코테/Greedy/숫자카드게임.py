n,m = map(int, input().split())


data = []
ans = -1
for _ in range(n):
    data.append(list(map(int, input().split())))
    compare  = min(data[-1])
    ans = max(ans, compare)
print(ans)