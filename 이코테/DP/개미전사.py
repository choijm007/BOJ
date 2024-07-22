n = int(input())
data = list(map(int,input().split()))
dp = [0]*101

dp[1]=data[0]
dp[2]=max(data[0], data[1])

for i in range(3,n+1):
    dp[i] = max(dp[i-1],dp[i-2]+data[i-1])

print(dp[n])