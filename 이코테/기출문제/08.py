data = list(map(str, input()))
data.sort()
num=0
result =""
for i in data:
    if i.isdecimal():
        num+=int(i)
    else:
        result+=i

print(result+str(num))
