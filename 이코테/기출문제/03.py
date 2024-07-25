## 다시풀어봐야함 밑에 풀이는 틀림

data = list(map(int,input()))

change=0
latest=data[0]
for i in range(1,len(data)):
    if latest != data[i]:
        change+=1
        latest=data[i]

if change==1:
    change=2
print(change//2)