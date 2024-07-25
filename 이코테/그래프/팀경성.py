n,m = map(int,input().split())

lst = [0]*(n+1)
for i in range(n+1):
    lst[i]=i

def parent(lst, a):
    if lst[a]!=a:
        lst[a]=parent(lst, lst[a])
    return lst[a]

def union(lst,a,b):
    a=parent(lst,a)
    b=parent(lst,b)
    if a<b:
        lst[b]=a
    else:
        lst[a]=b

for _ in range(m):
    a,b,c= map(int,input().split())
    if a==0:
        union(lst,b,c)
    elif a==1:
        if parent(lst,c) == parent(lst,b):
            print("YES")
        else:
            print("NO")


