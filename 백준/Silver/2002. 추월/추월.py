from collections import deque
input = __import__("sys").stdin.readline

n = int(input())
cars = deque()
answer = 0
remain_cars = set()

# check_illegal_list = []

for _ in range(n):
    inn = input()
    cars.append(inn)
    remain_cars.add(inn)

for _ in range(n):
    out =  input()

    first_car = cars.popleft()
    while not(first_car in remain_cars):
        first_car = cars.popleft()
    
    if first_car!=out:
        answer+=1
        remain_cars.discard(out)
        if first_car in remain_cars:
            cars.appendleft(first_car)

        # check_illegal_list.append(out)

    else:
        remain_cars.discard(out)

print(answer)
# print("illegal cars : ",check_illegal_list)