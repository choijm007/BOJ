s,n,k,x1,x2,y1,y2=map(int,input().split())


ans = [[0]*51for _ in range(51)]
def fractal(x,y,s):
    global ans

    if s==1:
        return
    if x+s<=x1 or y+s<=y1 or x>x2 or y>y2:
        return


    # 검은색 칠하기
    size = (s//n)*((n-k)//2)
    e = size+s//n*k -1

    r1 = max(x1, size+x)
    c1 = max(y1,size+y)
    r2=min(x2,e+x)
    c2 = min(y2,e+y)


    for i in range(r1,r2+1):
        for j in range(c1, c2+1):
            ans[i-x1][j-y1]=1



    for i in range(0,s,s//n):
        for j in range(0,s,s//n):
            if i>=size and i<=size and j>=size and j<=e:
                continue
            fractal(x+i,y+j,s//n)


fractal(0,0,n**s)
for i in range(x2-x1+1):
    for j in range(y2-y1+1):
        print(ans[i][j], end='')
    print()
