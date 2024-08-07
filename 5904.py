
n=int(input())

dp = [0]*2
dp[0]=3
dp[1]=10

start = 0
end = 2
cnt = 0
for i in range(2,n+1):
    dp.append(dp[i-1]+ i+3 +dp[i-1])
    if dp[i] >= n:
        end = dp[i]
        cnt = i
        break

def get_word(n):
    if n==1:
        return 'm'
    else:
        return 'o'

def back(k,n):
    res = dp[k-1]
    if k==0:
        res = 0
    if res < n <= k+3+res:
        print(get_word(n-res))
    elif n<=res:
        back(k-1,n)
    else:
        back(k-1, n - (res+k+3))

    return



back(cnt,n)
