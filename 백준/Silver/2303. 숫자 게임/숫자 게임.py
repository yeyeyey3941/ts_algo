import sys
input = sys.stdin.readline

n = int(input())
maxima_index = -1
maxima_value = -1
for current in range(n):
    n_th_cardlist = list(map(int,input().split(" ")))
    # check my Best
    total = sum(n_th_cardlist)
    local_sum  = 0
    for i in range(len(n_th_cardlist)):
        for j in range(i+1,len(n_th_cardlist)):
            now_value = total- n_th_cardlist[i] - n_th_cardlist[j]
            local_sum =  max(local_sum,now_value%10)
    # compare_maxima
    if maxima_value > local_sum:
        continue
    maxima_value = local_sum
    maxima_index = current

print(maxima_index+1)