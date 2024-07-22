n = int(input())

dir = list(map(str, input().split()))

def is_valid(y,x):
    return 0<=y<n and 0<=x<n


x,y=0,0
for d in dir:
    if d=='R':
        dx=1
        dy=0
    elif d=='U':
        dx=0
        dy=-1
    elif d=='L':
        dx=-1
        dy=0
    elif d=='D':
        dx=0
        dy=1

    x+=dx
    y+=dy
    if not is_valid(x,y):
        x-=dx
        y-=dy
    print(y+1, x+1)

print(y+1, x+1)