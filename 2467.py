n=int(input())

lst = list(map(int,input().split()))

startValue = 0
endValue = n-1
start =0
end =n-1

res =  abs(lst[end] + lst[start])
while start<end:
    compare = (lst[end] + lst[start])


    if abs(compare) < res:
        startValue = start
        endValue = end
        res = abs(compare)
        if res==0:
            break


    if compare<0:
        start+=1
    else:
        end-=1

print(lst[startValue], lst[endValue])