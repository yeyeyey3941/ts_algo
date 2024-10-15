def solution(n):
    field = [1]*1000001
    field[0] = field[1] = 0
    for i in range(2,1001):
        if field[i]:
            for j in range(i*i,1000001,i):
                field[j] = 0
    return sum(field[:n+1])