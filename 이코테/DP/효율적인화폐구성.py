n,m = map(int,input().split())


data = []
for _ in range(n):
    data.append(int(input()))
data.sort()
dp = [10001]*(m+1)
for i in data:
    if i<=m:

        dp[i]=1


for i in range(2,m+1):

    for j in data:
        if dp[i-j]==10001 or i<j:
            continue
        dp[i] = min(dp[i-j]+1,dp[i])
print(dp)
if dp[m]==10001:
    print(-1)
else:
    print(dp[m])

