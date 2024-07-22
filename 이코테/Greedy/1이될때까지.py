n,k = map(int, input().split())

ans=0

while n!=1:
    if n%k==0:
        n = n/k

    else:
        n-=1
    print(n)
    ans+=1

print(ans)