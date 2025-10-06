# 첫집과 끝집을 어떻게 처리할까?
# 첫집 현재 / 첫집 전값 / 두번째 현재 / 두번째 전값

def solution(money):
    first_current = [0]*(len(money)+1)
    second_current = [0]*(len(money)+1)
    first_not_current = [0]*(len(money)+1)
    second_not_current = [0]*(len(money)+1)
    
    first_current[1] = money[0]

    for i in range(1,len(money)-1):
        first_current[i+1] = first_not_current[i] + money[i]
        first_not_current[i+1] = max(first_not_current[i],first_current[i])
        second_current[i+1] = second_not_current[i] + money[i]
        second_not_current[i+1] = max(second_not_current[i],second_current[i])
    
    second_current[len(money)] = second_not_current[len(money)-1]+money[len(money)-1]

    return max(first_current[-2],first_not_current[-2],second_current[-1],second_not_current[-2])
