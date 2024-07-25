n = int(input())
data = list(map(int,input().split()))

data.sort()
data.reverse()
cnt =0
result =n

for i in data:
    result -=i
    if result<0:
        break
    cnt+=1


print(cnt)