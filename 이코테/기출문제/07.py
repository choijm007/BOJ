n = input()

mid = len(n)//2
a1=0
a2=0
for i in range(len(n)):
    if i<mid:
        a1 += int(n[i])
    else:
        a2+=int(n[i])

if a1==a2:
    print("LUCKY")
else:
    print("READY")