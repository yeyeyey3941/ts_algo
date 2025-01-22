'''
1. Each step save, check last step's floor set have N
2. predict before step's floor set
    2-1. If N th floor K, set of N-1 is [K-1 or K']
    There is K' such that K = K' + floor(K'/2) => K' = K * 2/3
    And K' may not be exist in N-1 th floor set(Since there is not K' such that K = K' + floor(K'/2))  


    if K = 3t , floor(k'/2) = t , K' = 2t, possible    
    if K = 3t+1 , floor(k'/2) = t , K' = 2t+1,possible
    if K = 3t+2 , floor(k'/2) = t+1 , K' = 2t+2, impossible

    
'''

# from math import floor

# n,k = map(int,input().split())

# answer = ["water","minigimbob"]
# answer_index = 0

# floor_set = set()
# floor_set.add(0)

# for _ in range(k):
#     new_floor = set()
#     for _ in range(len(floor_set)):
#         current_floor = floor_set.pop()
#         new_floor.add(current_floor+1)
#         new_floor.add(current_floor+floor(current_floor/2))
#     if n in new_floor: 
#         answer_index = 1
#         break
#     else:
#         floor_set = new_floor
#         print(floor_set)

#     if answer_index == 1:
#         break
# print(answer[answer_index])
    
# # -----------------------------------------------------------------------------------------


from math import floor

n,k = map(int,input().split())

answer = ["water","minigimbob"]
answer_index = 0

current_floor_set = set([n])


for i in range(k):
    before_floor_set = set()
    while current_floor_set:
        check_floor = current_floor_set.pop()
        if check_floor>0:
            before_floor_set.add(check_floor-1) 
        if check_floor%3 == 0 and check_floor>0:
            before_floor_set.add(2*check_floor//3)
        elif check_floor%3 == 1 and check_floor>1:
            before_floor_set.add(2*(check_floor-1)//3 + 1)
        else:
            "impossible"
            pass
    if 0 in before_floor_set:
        print(answer[1])
        break
    else:
        current_floor_set = before_floor_set
else:
    print(answer[0])            