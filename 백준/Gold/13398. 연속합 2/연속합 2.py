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