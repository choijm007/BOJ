n,m = map(int,input().split())
data = list(map(int,input().split()))


def get_len(l):
    result = 0
    for i in data:
        if i>l:
            result+=i-l
    return result


def binary(target):
    result = 0
    start =0
    end = max(data)
    while start<=end:
        mid = (start + end)//2

        if get_len(mid)<target:
            end = mid-1
        else:
            result = mid
            start = mid+1
    return result


print(binary(m))