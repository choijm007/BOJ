n,m = map(int,input().split())
data = list(map(int,input().split()))


result =0
def back(cnt, idx,lst):
    global result
    if cnt == 2:
        if lst[0] != lst[1]:
            print(lst)
            result +=1
        return
    for i in range(idx, len(data)):
        lst.append(data[i])
        back(cnt+1, i+1,lst)
        lst.pop()

back(0,0,[])
print(result)


tot = 0
for i in range(n-1):
    for j in range(i+1,n):
        if data[i] != data[j]:
            tot+=1
print(tot)