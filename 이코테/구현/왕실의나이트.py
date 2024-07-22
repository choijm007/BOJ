data = input()
x=int(data[1])-1
y=int(ord(data[0]))-int(ord('a'))

dy=[-2,-2,-1,1,2,2,-1,1]
dx=[-1,1,2,2,-1,1,-2,-2]

print(x,y)
def is_valid(ny,nx):
    return 0<=ny<8 and 0<=nx<8


result = 0
for i in range(8):
    ny = y+dy[i]
    nx = x+dx[i]
    if is_valid(ny,nx):
        result += 1

print(result)