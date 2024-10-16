def solution(target):
    answer = [False] * 100001
    answer[0] = [0,0]
    for i in range(1,21):
        answer[i] = [1, 1]
        answer[i*2] = [1,0]
        answer[i*3] = [1,0]
    answer[50] = [1,1]
    for i in range(23, target+1):
        if not(answer[i]):
            answer[i] = [999999,0]
            for j in range(1,21):
                for k in range(1,4):
                    if i - j*k >= 0:
                        if answer[i-j*k][0]+answer[j*k][0] < answer[i][0]:
                            answer[i] = [answer[i-j*k][0]+answer[j*k][0], answer[i-j*k][1]+answer[j*k][1]]
                        elif answer[i-j*k][0]+answer[j*k][0] == answer[i][0]:
                            answer[i] = [answer[i][0], max(answer[i-j*k][1]+answer[j*k][1],answer[i][1])]
            if i>50:
                if answer[i-50][0]+1 < answer[i][0]:
                    answer[i] = [answer[i-50][0]+1, answer[i-50][1]+1]
                elif answer[i-50][0]+1 == answer[i][0]:
                    answer[i] = [answer[i][0], max(answer[i-50][1]+1,answer[i][1])]
                
    # print(answer[:target+1])
    return answer[target]