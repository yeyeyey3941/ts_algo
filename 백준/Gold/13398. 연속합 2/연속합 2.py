
"""
1. 현재 인덱스의 값이 포함되는 연속된 최대값에 대해 
    1-1.이미 삭제를 한 경우:
        1-1-1.현재 인덱스의 값이 삭제된 경우(Not Delete CM)
        1-1-2.현재 인덱스의 값이 포함되는 경우(Delete CM+current) 
    1-2.삭제를 하지 않은 경우
        1-2-1.연속된 값의 합이 현재 인덱스의 값보다 작은 경우(current)
        1-2-2.연속된 값과 현재 값이 큰 경우(NDCM+current)
2. 여태의 최대값과 비교하여 최대값을 갱신한다.(maxima,NDCM,DCM)
"""


n = int(input())
number_list = list(map(int, input().split()))

dcm = 0 # delete_continuous_maxima 
ndcm = number_list[0] # not_delete_continuous_maxima
maxima = number_list[0] # 최대값

for i in range(1,n):
    current = number_list[i]
    dcm,ndcm= max(ndcm,current+dcm),max(ndcm+current,current)
    maxima = max(dcm,ndcm,maxima)
    # print(i,current,dcm,ndcm,maxima)
    
print(maxima)

# n = int(input())
# number_list = list(map(int, input().split()))

# maxima_list= number_list[:]
# dp = [[0, number_list[i]] for i in range(n)] # dp[i][0] = Delete Continuous Maxima, dp[i][1] = Not Delete Continuous Maxima

# for i in range(1,n):
#     dp[i][0] = max(dp[i-1][1],dp[i-1][0]+number_list[i])
#     dp[i][1] = max(dp[i-1][1]+number_list[i],number_list[i])
#     maxima_list[i] = max(dp[i][0],dp[i][1])
# if n == 1:
#     print(number_list[0])
# else:    
#     print(max(maxima_list))