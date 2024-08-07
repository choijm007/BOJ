import math

l,w,h = map(int,input().split())

n=int(input())

cube=[]
for _ in range(n):
    a,b = map(int,input().split())
    cube.append([a,b])
cube.reverse()
ok= False

def devide(ln,wd,ht):
    global cube, ok
    if ln==0 or wd==0 or ht==0:
        return 0
    mini = min(ln,wd,ht)
    t= int(math.log2(mini))
    for i in range(t,-1,-1):
        if cube[i][1]==0:
            continue
        cube[i][1]-=1
        T=pow(2,cube[i][0])
        return devide(ln-T,T,h) + devide(l,w-T,h) + devide(T,T,h-T) + 1
    ok = False
    return -1

res = devide(l,w,h)
if ok:
    print(res)
else:
    print(-1)


# before = 0
# ans = 0
# for a,b in cube:
#     before<<=3
#
#     cnt = (l>>a)*(w>>a)*(h>>a) - before
#     cnt = min(b,cnt)
#     before+=cnt
#     ans+=cnt
#
# if before == l*w*h:
#     print(ans)
# else:
#     print(-1)

