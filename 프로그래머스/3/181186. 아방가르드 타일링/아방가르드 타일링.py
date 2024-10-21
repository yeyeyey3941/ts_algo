def solution(n):
    # 라스트 타일을 기준으로 점화식 구현 fn = f(n-1) + 2f(n-2) + 5f(n-3)+ sum(2*f(n-4-3*k))+ sum(2*f(n-5-3*k))+ sum(4*f(n-6-3*k))
    array_size = n+1 if n>=6 else 6
    answer = [0]*(array_size)
    answer[0] = 1;answer[1] = 1;answer[2] = 3;answer[3] = 10;answer[4] = 23;answer[5] = 62
    if n<6:
        return answer[n]
    for i in range(6,n+1):
        answer[i] = (answer[i-1] + 2*answer[i-2] + 6*answer[i-3]+ answer[i-4] - answer[i-6])
    return answer[n] % 1000000007
