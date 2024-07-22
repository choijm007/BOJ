n = int(input())
data = list(map(int, input().split()))
m=int(input())
find = list(map(int,input().split()))
data.sort()

def binary(n,target):
    start = 0
    end = n-1
    while start<=end:
        mid = (start + end)//2
        if data[mid] == target:
            return "Yes"

        if data[mid]<target:
            start = mid
        else:
            end = mid-1
    return "No"


for i in find:
    print(binary(n,i), end = " ")