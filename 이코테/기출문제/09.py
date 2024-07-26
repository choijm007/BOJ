def solution(s):
    answer = len(s)

    for l in range(1,len(s)//2+1):
        res = ""
        latest = s[0:l]
        cnt = 1
        for j in range(l,len(s),l):
            print(latest,j,j+l,s[j:j+l])
            if s[j:j+l] == latest:
                cnt+=1
            else:

                if cnt!=1:
                    res+=str(cnt)

                res+=latest
                cnt=1
                latest = s[j:j+l]
        if cnt != 1:
            res += str(cnt)

        res += latest
        cnt = 1
        latest = s[j:j + l]
        answer = min(answer,len(res))
        print(res)
        print()




    return answer

print(solution("ababcdcdababcdcd"))