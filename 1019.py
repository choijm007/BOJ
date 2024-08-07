

def solv(first, second, plus):
    while first%10 != 0 and first<=second:
        tmp = first
        while tmp>0:
            ans[int(tmp%10)] += plus
            tmp//=10
        first+=1

    if first>second:
        return

    while second%10 != 9 and second>=first:
        tmp = second
        while tmp > 0:
            ans[int(tmp % 10)] += plus
            tmp //= 10
        second-=1

    cnt = (second//10-first//10 +1)
    for i in range(10):
        ans[i]+=cnt*plus

    solv(first//10, second//10, plus*10)

if __name__ == '__main__':
    n = int(input())

    ans = [0] * 10
    solv(1,n,1)
    for i in ans:
        print(i,end=' ')