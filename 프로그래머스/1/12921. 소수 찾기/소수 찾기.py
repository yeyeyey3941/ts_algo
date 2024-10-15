def solution(n):
    field = [1]*(n+1)
    field[0] = field[1] = 0
    for i in range(2,int(n**.5)+1):
        if field[i]:
            for j in range(i*i,n+1,i):
                field[j] = 0
    return sum(field)