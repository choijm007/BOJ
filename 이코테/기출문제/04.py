n=int(input())
data = list(map(int,input().split()))


result = set()
def back(cnt,visit,hap):
    if cnt == n:
        return
    for i in range(len(data)):
        if visit[i]==0:
            visit[i]=1
            result.add(hap+data[i])
            back(cnt+1,visit,hap+data[i])
            visit[i]=0


visit = [0]*(n)
back(0,visit,0)
print(result)