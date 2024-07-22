n = int(input())

ans = 0
for i in range(n+1):
    if i in (3,13,23):
       ans+=60*60
       continue

    for m in range(60):
        if m in (3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53):
            ans+=60
            continue
        for s in range(60):
            if s in (3, 13, 23, 30,31,32,33,34,35,36,37,38,39,43,53):
                
                ans+=1

print(ans)

